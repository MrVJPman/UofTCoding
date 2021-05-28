from critter import Critter
import random


class Bird(Critter):
    """A Bird that moves in the same randomly chosen vertical(north/south)
    direction for five turns, then the same randomly chosen
    horizontal(east/west) direction for five turns and then stays still for
    five turns. Its string representation is determined by its last move and it
    plays a winning move against a Mouse or Stone, else it plays rock."""
    def __init__(self):
        """Bird -> NoneType

        Initialize a Bird object.

        """
        self._next_step = 'center'
        self._step_repeated = 5

    def get_move(self):
        """Bird -> str

        Return the next move of the Bird object, moving in the same vertical
        direction(north/south) for five turns, same horizontal
        direction(east/west) for five turns, pause for five turns and repeat.

        """
        if self._step_repeated == 5:
            self._step_repeated = 1
            if self._next_step == 'center':
                self._next_step = random.choice(["north", "south"])
            elif self._next_step in ["north", "south"]:
                self._next_step = random.choice(["east", "west"])
            elif self._next_step in ["east", "west"]:
                self._next_step = "center"

        else:
            self._step_repeated += 1

        return self._next_step

    def duel(self, opponent):
        """(Bird, str) -> str

        Return the Bird object's attack when given an string representation
        of opponent. Plays scissors if opponent is 'Q'(Mouse), paper if
        opponent is '*'(Stone) and rock otherwise.

        """
        if opponent == "Q":
            return "scissors"
        elif opponent == "*":
            return "paper"
        else:
            return "rock"

    def get_color(self):
        """Bird -> str

        Return the string to draw the Bird object blue in colour.

        """
        return "blue"

    def __str__(self):
        """Bird -> str
        Return the string representation of the Bird object based on its last
        move. '&' if center or not moved yet, '^' if north, '>' if east, '<' if
        west or 'v' if south.

        """
        if self._next_step == "center":
            return "&"
        elif self._next_step == "north":
            return "^"
        elif self._next_step == "east":
            return ">"
        elif self._next_step == "west":
            return "<"
        elif self._next_step == "south":
            return "v"
