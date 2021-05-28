from critter import Critter


class Turtle(Critter):
    """A Turtle that slowly moves in a clockwise square and duels based on its
    last non-center move."""
    def __init__(self):
        """Turtle -> NoneType

        Initialize a Turtle object.

        """
        self._step_index = 0
        self._weapon = "scissors"

    def get_move(self):
        """Turtle -> str

        Return the next move of the Turtle object, moving in a clockwise four
        by four square with two pauses in between.

        """
        self._step_index += 1

        if self._step_index % 24 == 15:
            self._weapon = "rock"
        elif self._step_index % 24 == 3:
            self._weapon = "scissors"

        if self._step_index % 3 != 0:
            return "center"
        else:
            return ["west", "north",
                    "east", "south"][(self._step_index - 3) % 48 / 12]

    def duel(self, opponent):
        """(Turtle, str) -> str

        Return the Turtle object's attack when given an string representation
        of opponent. Plays scissors if last non-center move was horizontal
        (east/west) or if it hasn't moved yet and plays rock if last non-center
        move was vertical(north/south).

        """
        return self._weapon

    def get_color(self):
        """Turtle -> str

        Return the string to draw the Turtle object green in colour.

        """
        return "green"

    def __str__(self):
        """Turtle -> str

        Return the string representation of the Turtle object as @.

        """
        return "@"
