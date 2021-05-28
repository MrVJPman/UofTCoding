from critter import Critter


class Mouse(Critter):
    """A Mouse that moves in a zigzag pattern and always plays paper."""
    def __init__(self):
        """Mouse -> NoneType

        Initialize a Mouse object.

        """
        self._next_step = "north"

    def get_move(self):
        """Mouse -> str

        Return the next move of the Mouse object, alternating between north
        first and west second.

        """
        next_step = self._next_step
        if self._next_step == "north":
            self._next_step = "west"
        elif self._next_step == "west":
            self._next_step = "north"

        return next_step

    def duel(self, opponent):
        """(Mouse, str) -> str

        Return the Mouse object's attack when given an string representation
        of opponent. The Mouse object always plays paper.

        """
        return "paper"

    def get_color(self):
        """Mouse -> str

        Return the string to draw the Mouse object white in colour.

        """
        return "white"

    def __str__(self):
        """Mouse -> str

        Return the string representation of the Mouse object as Q.

        """
        return "Q"
