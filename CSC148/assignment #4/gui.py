from world import World
from Tkinter import Tk, Canvas, Button, Frame, Label


class GuiWorld(World):
    def __init__(self, width, height, **kwargs):
        World.__init__(self, width, height, use_color=False)
        master = Tk()
        master.wm_title("CSC148: Critter world")

        tile_height = 15
        tile_width = 15
        canvas_width = tile_width * (self._width + 1)
        window_height = tile_height * (self._height + 1)
        canvas = Canvas(master,
                        width=canvas_width,
                        height=window_height,
                        background="black",
                        borderwidth=1,
                        relief="sunken")
        canvas.pack(side="left")

        sidebar = Frame(master)
        sidebar.pack(side="right", fill="both", expand=True)

        # Set up scoreboard
        scores = Frame(sidebar)
        scores.pack(side="top", fill="y", expand=True)

        self._score_labels = {}
        for category in ['alive', 'kills', 'score']:
            f = Frame(scores, borderwidth=2, relief="raised")
            f.pack(padx=5, pady=5)
            Label(f, text="%s:" % category.upper(), anchor="w", padx=5,
                  font=("Courier New", "14", "bold")).pack(side="left")
            self._score_labels[category] = (f, {})

        self._step_label = Label(scores, text="Step: %d" % self._step,
                                 anchor="w", padx=10,
                                 font=("Courier New", "14"))
        self._step_label.pack(side="left")

        # Add buttons
        buttons = Frame(sidebar, borderwidth=1, relief="sunken")
        buttons.pack(side="bottom")
        Button(buttons, text="Step", command=self.update).pack(side="left")
        Button(buttons, text="Run", command=self.run).pack(side="left")
        Button(buttons, text="Stop", command=self.stop).pack(side="left")

        # Add critter letters to map
        self._tile_text = {}
        for row in self._map:
            for tile in row:
                self._tile_text[tile] = \
                    canvas.create_text(tile_width * (tile.x + 1),
                                       tile_height * (tile.y + 1),
                                       text=str(tile),
                                       fill=tile.get_color(),
                                       font=("Courier New", "16"))

        self._scores = scores
        self._canvas = canvas
        self._master = master
        self._loop_times = 0
        self._delay = 100

    def refresh(self):
        World.refresh(self)

        # Update step count
        self._step_label['text'] = "Step: %d" % self._step

        # Update critter strings in world
        for row in self._map:
            for tile in row:
                tile_text = self._tile_text[tile]
                self._canvas.itemconfig(tile_text,
                                        text=str(tile),
                                        fill=tile.get_color())

        # Update scores
        stats = self._get_stats()
        for category, (frame, labels) in self._score_labels.iteritems():
            max_score = max([score for species, score in stats[category]])
            for species, score in stats[category]:
                line = "%-8s: %2d" % (species, score)
                font = ["Courier New", "12"]
                if score == max_score:
                    font.append("bold")

                if species in labels:
                    label = labels[species]
                    label['text'] = line
                else:
                    label = Label(frame, text=line, anchor="nw",
                                  font=font)
                    label.pack()
                    labels[species] = label

                label.configure(font=font)

    def update(self):
        World.update(self)
        self.refresh()
        self._loop_times -= 1
        if self._loop_times > 0:
            self._canvas.after(self._delay, self.update)

    def stop(self):
        self._loop_times = 0

    def run(self, prompt=False, delay=0.1, n=1000):
        self.refresh()
        if not prompt and n > 0:
            self._delay = int(delay * 1000)
            self._loop_times = n
            self._canvas.after(self._delay, self.update)

        self._master.mainloop()
