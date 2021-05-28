from collections import deque


class ShelfFullError(Exception):
    pass


class ShelfEmptyError(Exception):
    pass


class Shelf(object):
    """A refrigerator shelf, capable of being stocked by a clerk from the back
    or having drinks added or removed from the front"""
    def __init__(self, capacity):
        """(Shelf, int) -> NoneType
        Initialize a shelf capable of holding up to capacity Drinks.
        """
        self._data = deque()
        self._capacity = capacity

    def put_drink(self, drink):
        """(Shelf, Drink) -> NoneType
        Add drink to the front of the shelf
        Raises ShelfFullError if the shelf is full
        """
        if len(self) < self._capacity:
            self._data.append(drink)
        else:
            raise ShelfFullError()

    def take_drink(self):
        """Shelf -> Drink
        Remove and return the drink at the front of the shelf
        Raises ShelfEmptyError if the shelf is empty
        """
        if len(self) > 0:
            return self._data.pop()
        else:
            raise ShelfEmptyError()

    def stock_drink(self, drink):
        """(Shelf, Drink) -> NoneType
        Add drink to the back of the shelf
        Raises ShelfFullError if the shelf is full
        """
        if self.is_full():
            raise ShelfFullError()
        else:
            self._data.appendleft(drink)

    def is_empty(self):
        """Shelf -> bool
        Return whether or not the shelf has no drinks on it
        """
        return len(self) == 0

    def is_full(self):
        """Shelf -> bool
        Return whether or not the shelf has the maximum number of drinks on it
        """
        return len(self) >= self._capacity

    def __len__(self):
        """Shelf -> int
        Return number of drinks on shelf
        """
        return len(self._data)

    def __str__(self):
        """Shelf -> str
        Return string representation of shelf
        """
        return '[back] %s [front]' % ', '.join([str(o) for o in self._data])
