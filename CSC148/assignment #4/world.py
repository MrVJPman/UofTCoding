from collections import defaultdict
from random import sample, choice, shuffle
from time import sleep


class World(object):
    def __init__(self, width, height, use_color=True):
        self._height = height
        self._width = width
        self._map = [[Tile(col_i, row_i, use_color=use_color)
                      for col_i in range(width)]
                     for row_i in range(height)]
        self._directions = set(["north", "south", "east", "west", "center"])
        self._valid_attacks = set(["forfeit", "rock", "paper", "scissors"])
        self.use_color = use_color

        self._step = 0
        self._critters = {}
        self._counts = defaultdict(int)
        self._kills = defaultdict(int)
        self._attacks = {("rock", "paper"): 1,
                         ("paper", "rock"): 0,
                         ("rock", "scissors"): 0,
                         ("scissors", "rock"): 1,
                         ("paper", "scissors"): 1,
                         ("scissors", "paper"): 0,
                         ("forfeit", "rock"): 1,
                         ("forfeit", "paper"): 1,
                         ("forfeit", "scissors"): 1,
                         ("rock", "forfeit"): 0,
                         ("paper", "forfeit"): 0,
                         ("scissors", "forfeit"): 0}

    def generate(self, Critter, n):
        open = []
        for row in self._map:
            open.extend([tile for tile in row if not tile])

        tiles = sample(open, n)
        for tile in tiles:
            critter = Critter()
            tile.add(critter)
            self._critters[critter] = tile
            self._counts[type(critter)] += 1
            # Decorate critter
            critter.x = tile.x
            critter.y = tile.y
            critter.world_height = self._height
            critter.world_width = self._width
            critter.neighbors = {}

    def _update_critter_neighbors(self, critter):
        critter.neighbors.clear()
        tile = self._critters[critter]
        for dir in self._directions:
            if dir != "center":
                critter.neighbors[dir] = str(self._adjacent(tile, dir))

    def _adjacent(self, tile, dir):
        dest_x = tile.x
        dest_y = tile.y
        if dir == "north":
            dest_y = (dest_y - 1) % self._height
        elif dir == "south":
            dest_y = (dest_y + 1) % self._height
        elif dir == "east":
            dest_x = (dest_x + 1) % self._width
        elif dir == "west":
            dest_x = (dest_x - 1) % self._width

        return self._map[dest_y][dest_x]

    def refresh(self):
        # Update all critter neighbors
        for critter in self._critters:
            self._update_critter_neighbors(critter)

    def update(self):
        self._step += 1

        # Move critters, resolving fights
        critters = self._critters.keys()
        shuffle(critters)
        for critter in critters:
            # Skip if died already this turn
            if critter not in self._critters:
                continue

            src = self._critters[critter]

            move = critter.get_move()
            assert move in self._directions, \
                "%s returned invalid move: %s" % (type(critter).__name__, move)

            dest = self._adjacent(src, move)

            # Move critter (if not "center")
            if dest != src:
                src.remove()
                if dest:
                    # Battle if there is someone already there
                    opponent = dest.remove()
                    winner, loser = self._battle(critter, opponent)
                    # Remove loser
                    del self._critters[loser]
                    self._counts[type(loser)] -= 1
                    self._kills[type(winner)] += 1
                    critter = winner

                # Put winner/critter in dest
                dest.add(critter)
                self._critters[critter] = dest

                # Update attributes of moved critter
                critter.x = dest.x
                critter.y = dest.y
                self._update_critter_neighbors(critter)
                # Update neighbors of nearby critters
                for (to_tile, from_tile) in [("north", "south"),
                                             ("south", "north"),
                                             ("east", "west"),
                                             ("west", "east")]:
                    # Nearby source tile, neighbor is now empty
                    tile = self._adjacent(src, to_tile)
                    if tile:
                        tile.get().neighbors[from_tile] = str(src)

                    # Nearby destination tile, neighbor is now winner
                    tile = self._adjacent(dest, to_tile)
                    if tile:
                        tile.get().neighbors[from_tile] = str(dest)

    def _battle(self, first, second):
        def check_attack(critter, opponent_str):
            attack = critter.duel(opponent_str)
            assert attack in self._valid_attacks, \
                "%s returned invalid attack: %s" % \
                (type(critter).__name__, attack)
            return attack

        attack1 = check_attack(first, str(second)[:1])
        attack2 = check_attack(second, str(first)[:1])

        # Choose winner
        if attack1 == attack2:
            winner_i = choice(range(2))
        else:
            winner_i = self._attacks[(attack1, attack2)]

        winner = [first, second][winner_i]
        loser = [first, second][1 - winner_i]
        # Notify players
        winner.won()
        loser.lost()
        return winner, loser

    def _get_stats(self):
        stats = {}
        # Get critter classes, sorted by name
        species = [cls for name, cls in
                   sorted([(cls.__name__, cls) for cls in self._counts])]

        stats['alive'] = [(cls.__name__, self._counts[cls]) for cls in species]
        stats['kills'] = [(cls.__name__, self._kills[cls]) for cls in species]
        stats['score'] = [(cls.__name__, self._counts[cls] + self._kills[cls])
                          for cls in species]
        return stats

    def __str__(self):
        lines = [' '.join([str(tile) for tile in row])
                 for row in self._map]

        # Add border
        top = "+-%s-+" % (" ".join(["-"] * self._width))
        map = [top] + ['| %s |' % line for line in lines] + [top]

        stats = self._get_stats()
        leaderboard = []

        def add_stats(stats, death=False):
            max_score = max([score for name, score in stats])
            for name, score in stats:
                line = "%-8s: %d" % (name, score)
                # Bold the max values
                if self.use_color:
                    if score == max_score:
                        line = Colorize(line, bold=True)
                    elif death and score == 0:
                        line = Colorize(line, "red")

                leaderboard.append(line)

        # Add counts
        leaderboard.extend(["ALIVE:"])
        add_stats(stats['alive'], death=True)

        # Add kills
        leaderboard.extend(["", "KILLS:"])
        add_stats(stats['kills'])

        # Add scores
        leaderboard.extend(["", "SCORE:"])
        add_stats(stats['score'])

        leaderboard.extend(["", "Step: %d" % self._step])

        # Insert lines onto right side of map
        for i, line in enumerate(leaderboard):
            map[i + 1] += "  %s" % line
            #map[-(i + 1)] += "  %s" % line

        return '\n'.join(map)

    def run(self, prompt=False, delay=0.1, n=1000):
        self.refresh()

        print self
        for i in range(n):
            if delay:
                sleep(delay)

            if prompt:
                if raw_input("Press ENTER to go to the next time step"
                             " (or 'quit' to exit)... ").strip() == 'quit':
                    break

            self.update()
            print self


class Colorize(object):
    colors = {"clear": "\033[0m",
              "bold": "\033[1m",
              "black": "\033[30m",
              "red": "\033[31m",
              "green": "\033[32m",
              "yellow": "\033[33m",
              "blue": "\033[34m",
              "magenta": "\033[35m",
              "cyan": "\033[36m",
              "white": "\033[37m",
              "gray": "\033[30m",
              "default": "\033[39m"}

    def __init__(self, string, color=None, bold=False):
        parts = [str(string)]
        if color is not None:
            assert color in self.colors, \
                "Color must be one of: %s" % sorted(self.colors.keys())
            parts.insert(0, self.colors[color])

        if bold:
            parts.insert(0, self.colors["bold"])

        if color is not None or bold:
            parts.append(self.colors["clear"])

        self.s = ''.join(parts)

    def __str__(self):
        return self.s


class Tile(object):
    def __init__(self, x, y, use_color=True):
        self.x = x
        self.y = y
        self.critter = None
        self.use_color = use_color

    def __str__(self):
        if self:
            s = str(self.critter)[:1]
            if self.use_color:
                color = self.get_color()
                s = str(Colorize(s, color, bold=True))

            return s
        else:
            return " "

    def get_color(self):
        if self:
            color = self.critter.get_color()
            assert color in Colorize.colors, \
                "%s returned invalid color: %s\nMust be one of: %s" % \
                (type(self.critter).__name__, color, sorted(Colorize.colors))
            return color
        else:
            return "black"

    def add(self, critter):
        assert self.critter is None
        self.critter = critter

    def remove(self):
        critter = self.critter
        self.critter = None
        return critter

    def get(self):
        return self.critter

    def __nonzero__(self):
        return self.critter is not None
