from critter import Critter


class Stone(Critter):
    """A very simple Critter that just sits there."""
    def duel(self, opponent):
        """(Stone, str) -> str
        Always play rock
        """
        return "rock"

    def get_color(self):
        """Stone -> str
        Gray in color
        """
        return "gray"

    def __str__(self):
        """Stone -> str
        Appear as an asterisk
        """
        return "*"
