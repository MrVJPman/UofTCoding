from critter import Critter


class Jellyfish(Critter):
    def __init__(self):
        self._next_dir = "east"

    # color: yellow
    # string
    def __str__(self):
        if self._next_dir == "east":
            return "]"
        else:
            return ">"

    # duel
    def duel(self, opponent):
        return "scissors"

    # move
    def get_move(self):
        """Jellyfish -> str
        Goes east, center, repeat
        """
        next_dir = self._next_dir
        # Update stored direction
        if next_dir == "east":
            self._next_dir = "center"
        else:
            self._next_dir = "east"

        return next_dir

# Here's another way to implement the same class, using a step counter
class Jellyfish(Critter):
    def __init__(self):
        self._step = 0

    # color: yellow
    # string
    def __str__(self):
        return "]>"[self._step % 2]

    # duel
    def duel(self, opponent):
        return "scissors"

    # move
    def get_move(self):
        """Jellyfish -> str
        Goes east, center, repeat
        """
        self._step += 1
        return ["center", "east"][self._step % 2]
