from critter import Critter
import random


class Ant(Critter):
    """An Ant that moves randomly and duels randomly."""
    def get_move(self):
        """Ant -> str

        Return the next move of the Ant object, chosen randomly from north,
        south, east, west or center.

        """
        return random.choice(["north", "south", "east", "west", "center"])

    def duel(self, opponent):
        """(Ant, str) -> str

        Return the Ant object's attack when given an string representation
        of opponent. The Ant object plays randomly from rock, paper or
        scissors.

        """
        return random.choice(["rock", "paper", "scissors"])

    def get_color(self):
        """Ant -> str

        Return the string to draw the Ant object red in colour.

        """
        return "red"

    def __str__(self):
        """Ant -> str

        Return the string representation of the Ant object as %.

        """
        return "W"#"%"
