class Critter(object):
    """The super class for all critters in the critter world"""
    # Every Critter must implement the following three methods,
    # which together (with __init__) constitute the Critter's behavior.
    def get_move(self):
        """Critter -> str
        Return the next move of the Critter object.
        """
        return "center"

    def duel(self, opponent):
        """(Critter, str) -> str
        Return the Critter's attack when dueling against an opponent
        with the given string representation.
        """
        return "forfeit"

    def get_color(self):
        """Critter -> str
        Return the color to draw the Critter.
        """
        return "yellow"

    def __str__(self):
        """Critter -> str
        Return the string representation of the Critter
        (only the first character will be used)
        """
        return "."

    # Your critter can implement the following methods to have
    # more complex behavior.
    def won(self):
        """Critter -> NoneType
        Called on a Critter object after it wins a duel.
        """
        pass

    def lost(self):
        """Critter -> NoneType
        Called on a Critter object after it loses a duel.
        """
        pass

    # Every Critter also has the following methods. You can either use the
    # methods, or the public attributes that they call. The public instance
    # variables are maintained by the simulator, so you can access them if
    # you would like.
    #
    # None of the default critters use these methods/variables, but your Wolf
    # class can use them to have much more complex and interesting behavior.
    #
    # Note: these instance variables aren't set until after the critter is
    # created, so you can't access them in __init__.
    def get_neighbor(self, direction):
        """(Critter, str) -> str
        Return what the Critter's neighbor in a given direction looks like
        (its str) or ' ' if there is nothing there.
        """
        return self.neighbors[direction]

    def get_x(self):
        """Critter -> int
        Return the x-coordinate of the Critter (left edge is 0)
        """
        return self.x

    def get_y(self):
        """Critter -> int
        Return the y-coordinate of the Critter (top edge is 0)
        """
        return self.y

    def get_width(self):
        """Critter -> int
        Return the width of the Critter's world
        """
        return self.world_width

    def get_height(self):
        """Critter -> int
        Return the height of the Critter's world
        """
        return self.world_height
