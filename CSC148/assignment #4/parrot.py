from bird import Bird
import random


class Parrot(Bird):
    """A Parrot that behaves very similar to a bird. The only exception is that
    its string representation is the same as its last defeated opponent, else
    a question mark(?)."""
    def __init__(self):
        """Parrot -> NoneType
        Initialize a Parrot object.
        """
        Bird.__init__(self)
        self._last_opponent = '?'

    def duel(self, opponent):
        """(Parrot, str) -> str
        Return the Parrot object's attack when given an string representation
        of opponent. Plays scissors if opponent is 'Q'(Mouse), paper if
        opponent is '*'(Stone) and rock otherwise.

        """
        self._last_opponent = opponent
        return Bird.duel(self, opponent)

    def get_color(self):
        """Parrot -> str
        Return the string to draw the Parrot object yellow in colour.

        """
        return "yellow"

    def __str__(self):
        """Parrot -> str
        Return the string representation of the Parrot object based on its last
        defeated opponent, else a question mark(?) if it has not faced an
        opponent yet.

        """
        return self._last_opponent
