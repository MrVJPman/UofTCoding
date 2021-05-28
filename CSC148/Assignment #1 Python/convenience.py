from shelf import Shelf
import random


class Refrigerator(object):
    """A refrigerator, capable of having shelves with corresponding
    capacities and drinks can be added to it. Drinks can age inside
    the refrigerator and can be taken out if they have expired.
    """
    def __init__(self, shelf_capacities):
        """(Refrigerator, list(ints)) -> NoneType

        Initialize a Refrigerator object with number of shelves equal to the
        number of ints in shelf_capacities. The capacity of each shelf is
        determined by its index and is equal to the integer returned when
        calling the index of the shelf_capacity list.

        """
        self._data = []
        for shelf_capacity_value in shelf_capacities:
            shelf = Shelf(shelf_capacity_value)
            self._data.append(shelf)

    def __iter__(self):
        """Refrigerator -> Iterator(Shelfs)

        Return an iterator that iterates over the Shelf objects inside the
        Refrigerator object.

        """
        return iter(self._data)

    def __len__(self):
        """Refrigerator -> int

        Return the number of Shelf objects inside the Refrigerator object.

        """
        return len(self._data)

    def __str__(self):
        """Refrigerator -> int

        Return the string representation of Refrigerator object. The string
        contains information on each of Shelf object inside the Refrigerator
        object, including ordering of drinks, their names and their number of
        days before expiration.

        """
        self._string = ""
        for index in range(len(self._data)):
            self._string += "shelf %d: %s" % (index, self._data[index]) + "\n"
        return self._string[:-1]

    def stock_drinks(self, drinks):
        """(Refrigerator, list(Drinks)) -> NoneType

        Distributes the Drink objects in drinks evenly among Shelf objects in
        Refrigerator object. If a Shelf object is full, the distribution is
        skipped to the next non-full Shelf object.

        """
        drinks_copy = drinks[:]
        while drinks_copy:
            for shelf in self._data:
                if not shelf.is_full():
                    drink = drinks_copy.pop(0)
                    shelf.stock_drink(drink)

    def age_drinks(self):
        """Refrigerator -> NoneType

        Lower the days before expiration of all Drink objects inside
        Refrigerator object by one.

        """
        for shelf in self._data:
            for index in range(len(shelf)):
                drink = shelf.take_drink()
                drink.age_one_day()
                shelf.stock_drink(drink)

    def cull_drinks(self):
        """Refrigerator -> int

        Remove all Drink objects that has expired and return the number of
        Drink objects removed.

        """
        number_of_culled_drinks = 0
        for shelf in self._data:
            for index in range(len(shelf)):
                drink = shelf.take_drink()
                if drink.is_expired():
                    number_of_culled_drinks += 1
                else:
                    shelf.stock_drink(drink)
        return number_of_culled_drinks


class Drink(object):
    """A drink, capable of being named, and assigned a limited number of days
    before it expires.
    """
    def __init__(self, name, days_until_expiry):
        """(Drink, str, int) -> NoneType

        Initialize a Drink object called name with days_until_expiry days
        before the drink expires.

        """
        self._name = name
        self._days_left = days_until_expiry

    def __str__(self):
        """Drink -> str

        Return the string representation of Drink object. The string reveals
        the name and days before expiration of the Drink object.

        """
        return "%s (%d day(s) until expiry)" % (self._name, self._days_left)

    def days_until_expiry(self):
        """Drink -> int

        Return the number of days before expiration of Drink object.

        """
        return self._days_left

    def age_one_day(self):
        """Drink -> NoneType

        Reduce the number of days before expiration by one for the Drink
        object.

        """
        self._days_left -= 1

    def is_expired(self):
        """Drink -> bool

        Return True if the Drink object has expired, False Otherwise.

        """
        return self._days_left < 0


class Customer(object):
    """A customber, capable of being simple, ambivalent, or determined. Always
    checking if a refridgerator is empty at the start.
    """
    def refrigerator_check_empty(self, refridgerator):
        """Refrigetator -> bool

        Return True if refrigerator lacks any Shelf objects or all the Shelf
        objects in refrigerator lacks any Drink objects. False otherwise.

        """
        for shelf in refridgerator:
            if len(shelf) >= 1:
                return False
        return True


class SimpleCustomer(Customer):
    """A simple customer, whom attempts to takes the first drink from the
    first non-empty shelf inside a refrigerator.
    """
    def get_drink(self, refridgerator):
        """(SimpleCustomer, Refrigerator) -> Drink/NoneType

        Remove and return the first Drink object in the first non-empty Shelf
        object in refrigerator. Returns None if no Drink objects are present in
        refrigerator.

        """
        if self.refrigerator_check_empty(refridgerator):
            return None
        for shelf in refridgerator:
            if not shelf.is_empty():
                return shelf.take_drink()


class AmbivalentCustomer(Customer):
    """An amivalent customer, whom attempts to takes the first drink from
    a random non-empty shelf inside a refrigerator.
    """
    def get_drink(self, refridgerator):
        """(AmbivalentCustomer, Refrigerator) -> Drink / NoneType

        Remove and return the first Drink object in a random non-empty Shelf
        object in refrigerator. Returns None if no Drink objects are present in
        refrigerator.

        """
        if self.refrigerator_check_empty(refridgerator):
            return None
        list_of_shelves = []
        for shelf in refridgerator:
            if not shelf.is_empty():
                list_of_shelves.append(shelf)
        randomly_selected_shelf = random.choice(list_of_shelves)
        return randomly_selected_shelf.take_drink()


class DeterminedCustomer(Customer):
    """A determined customer, whom attempts to take the frontmost drink
    with the greatest days before expiration from all non-empty shelves inside
    a refrigerator.
    """
    def get_drink(self, refridgerator):
        """(DeterminedCustomer, Refrigerator) -> Drink / NoneType

        Remove and return the first Drink object amongst all non-empty Shelf
        in Refrigerator with the greatest number of days before expiration.
        Shelf objects have their frontmost Drink objects swapped with the
        earliest succeeding Shelf object if succeeding Shelf object's own
        frontmost Drink object has a greater number of days before expiration
        and frontmost Drink objects in all preceeding Shelf Objects has a
        lesser number of days before expiration. Returns None if no Drink
        objects are present in refrigerator.

        """
        if self.refrigerator_check_empty(refridgerator):
            return None
        list_of_shelves = []
        old_drink = None
        for shelf in refridgerator:
            if not shelf.is_empty():
                new_drink = shelf.take_drink()
                if old_drink == None:
                    old_drink = new_drink
                elif new_drink.days_until_expiry() > \
                     old_drink.days_until_expiry():
                    shelf.put_drink(old_drink)
                    old_drink = new_drink
                else:
                    shelf.put_drink(new_drink)
        return old_drink
