# No need to import Critter!
from jellyfish import Jellyfish


class ManOfWar(Jellyfish):
    def __init__(self):
        # Call the jellyfish constructor to initalize our instance variables
        Jellyfish.__init__(self)
        # Also record whether or not we've dueled yet
        self._has_dueled = False

    def duel(self, opponent):
        # Use the Jellyfish duel, but remember that we've dueled, first
        self._has_dueled = True
        return Jellyfish.duel(self, opponent)

    def get_color(self):
        return "blue"

    def get_move(self):
        # If we've dueled, use the Jellyfish move
        if self._has_dueled:
            return Jellyfish.get_move(self)
        else:
            # Otherwise, just return center
            return "center"

    # NOTE: This isn't perfectly correct, since the ManOfWar's __str__
    # makes it look like it's about to move "east" the whole time it
    # is returning center before it gets into a fight. This is probably
    # alright for this example. :)
