import unittest

from shelf import Shelf

from convenience import Drink, Refrigerator

class DrinkTests(unittest.TestCase):
    """Test behaviour of lots of drinks."""
    def setUp(self):
        self.names = ["cola", "Dr. pepper", "orange juice", ""]
        self.expiries = [-2, 0, 1, 10]
        self.drinks = [Drink(name, expiry) for name, expiry
                       in zip(self.names, self.expiries)]

    def testStr(self):
        """Testing __str__() on many drinks."""
        for drink, name, expiry in zip(self.drinks, self.names, self.expiries):
            self.assertEqual(str(drink),
                             '%s (%d day(s) until expiry)' % (name, expiry))

    def testDaysUntilExpiry(self):
        """Testing days_until_expiry() on many drinks."""
        for drink, expiry in zip(self.drinks, self.expiries):
            self.assertEqual(drink.days_until_expiry(), expiry)

    def testAgeOneDay(self):
        """Test age_one_day() and days_until_expiry() on many drinks."""
        for drink, expiry in zip(self.drinks, self.expiries):
            self.assertEqual(drink.age_one_day(), None)
            self.assertEqual(drink.days_until_expiry(), expiry - 1)

    def testIsExpired(self):
        """Testing is_expired() on many drinks."""
        for drink, expiry in zip(self.drinks, self.expiries):
            self.assertEqual(drink.is_expired(), expiry < 0)


def no_whitespace(s):
    return s.translate(None, "\n\t ")

# Test Refrigerator class
class RefrigeratorSetupTests(unittest.TestCase):
    """Test basic setup behavior of lots of Refrigerators."""
    def setUp(self):
        self.capacities_list = [[], [0], [0, 0, 0], [1], [1, 2, 1], [2, 0, 5]]
        self.fridges = [Refrigerator(capacities)
                        for capacities in self.capacities_list]

    def testIter(self):
        """Testing iter() on lots of Refrigerators."""
        for fridge, capacities in zip(self.fridges, self.capacities_list):
            it = iter(fridge)
            for i in capacities:
                self.assertEqual(type(it.next()), Shelf)

            self.assertRaises(StopIteration, it.next)

    def testLen(self):
        """Testing len() on lots of refrigerators"""
        for fridge, capacities in zip(self.fridges, self.capacities_list):
            self.assertEqual(len(fridge), len(capacities))

    def testStrGenerous(self):
        """Testing str() on lots of refrigerators"""
        for fridge in self.fridges:
            expected = '\n'.join(['shelf %d: %s' % (i, shelf)
                                  for (i, shelf) in enumerate(fridge)])
            self.assertEqual(no_whitespace(str(fridge)),
                             no_whitespace(expected))

    def testStrStrict(self):
        """Testing str() on lots of refrigerators"""
        for fridge in self.fridges:
            expected = '\n'.join(['shelf %d: %s' % (i, shelf)
                                  for (i, shelf) in enumerate(fridge)])
            self.assertEqual(str(fridge), expected)


class RefrigeratorNoCapacityTests(unittest.TestCase):
    def testRobustness(self):
        """Testing stock_drinks, age_drinks, and cull_drinks on Refrigerators
        without capacity (just make sure nothing breaks or hangs)."""
        capacities_list = [[], [0], [0, 0, 0]]
        fridges = [Refrigerator(capacities)
                   for capacities in capacities_list]

        for fridge in fridges:
            fridge.stock_drinks([])
            fridge.age_drinks()
            fridge.cull_drinks()


class RefrigeratorStockTests(unittest.TestCase):
    def setUp(self):
        capacities = [1]
        self.fridge = Refrigerator(capacities)
        self.drinks = [Drink("a", 1)]
        self.stock_indices = [[0]]
        self.fridge.stock_drinks(self.drinks)

    def safe_stock(self, copy_drinks=True):
        drinks = self.drinks[:] if copy_drinks else self.drinks
        self.fridge.stock_drinks(drinks)

    def testStockingAndCheckSameDrinks(self):
        """Test stocking order and check drink memory addresses"""
        for shelf, indices in zip(self.fridge, self.stock_indices):
            for i in indices:
                self.assertEqual(shelf.take_drink(), self.drinks[i])

    def testAgeDrinks(self):
        """Test that aging drinks maintains order and actually ages drinks"""
        # Store expiries before aging
        expiries = [drink.days_until_expiry() for drink in self.drinks]
        self.fridge.age_drinks()
        for shelf, indices in zip(self.fridge, self.stock_indices):
            for i in indices:
                drink = shelf.take_drink()
                self.assertEqual(drink, self.drinks[i])
                self.assertEqual(drink.days_until_expiry(), expiries[i] - 1)

    def testAgeDrinksTwice(self):
        """Test that aging drinks maintains order and actually ages drinks"""
        # Store expiries before aging
        expiries = [drink.days_until_expiry() for drink in self.drinks]
        self.fridge.age_drinks()
        self.fridge.age_drinks()
        for shelf, indices in zip(self.fridge, self.stock_indices):
            for i in indices:
                drink = shelf.take_drink()
                self.assertEqual(drink, self.drinks[i])
                self.assertEqual(drink.days_until_expiry(), expiries[i] - 2)


class RefrigeratorJustEnoughSpaceTests(RefrigeratorStockTests):
    def setUp(self):
        capacities = [2, 2, 2]
        self.fridge = Refrigerator(capacities)
        self.drinks = [Drink("a", 1), Drink("b", 2), Drink("c", 3),
                       Drink("d", 4), Drink("e", 5), Drink("f", 6)]
        self.stock_indices = [[0, 3], [1, 4], [2, 5]]
        self.safe_stock()

    def testStockingByStr(self):
        """Test stocking order using str(drink)"""
        while self.drinks:
            for i, shelf in enumerate(self.fridge):
                self.assertEqual(str(shelf.take_drink()),
                                 str(self.drinks.pop(0)))

class RefrigeratorExtraSpaceTests(RefrigeratorStockTests):
    def setUp(self):
        capacities = [1, 10, 10]
        self.fridge = Refrigerator(capacities)
        self.drinks = [Drink("a", 1), Drink("b", 2), Drink("c", 3),
                       Drink("d", 4), Drink("e", 5), Drink("f", 6)]
        self.stock_indices = [[0], [1, 3, 5], [2, 4]]
        self.safe_stock()


class RefrigeratorSkipShelfTests(RefrigeratorStockTests):
    def setUp(self):
        capacities = [10, 0, 10]
        self.fridge = Refrigerator(capacities)
        self.drinks = [Drink("a", 1), Drink("b", 2), Drink("c", 3),
                       Drink("d", 4), Drink("e", 5), Drink("f", 6),
                       Drink("g", 7)]
        self.stock_indices = [[0, 2, 4, 6], [], [1, 3, 5]]
        self.safe_stock()


class RefrigeratorCullDrinksTests(RefrigeratorStockTests):
    def setUp(self):
        capacities = [3, 3]
        self.fridge = Refrigerator(capacities)
        self.drinks = [Drink("a", 1), Drink("b", -1), Drink("c", 0),
                       Drink("d", 4), Drink("e", 5)]
        self.stock_indices = [[0, 2, 4], [1, 3]]
        self.safe_stock()

    def testCullDrinksReturnOne(self):
        self.assertEqual(self.fridge.cull_drinks(), 1)

    def testCullDrinksReturnZero(self):
        self.fridge.cull_drinks()
        self.assertEqual(self.fridge.cull_drinks(), 0)

    def testCullDrinksReturnWithAge(self):
        self.fridge.age_drinks()
        self.fridge.age_drinks()
        self.assertEqual(self.fridge.cull_drinks(), 3)

    def testCullDrinks(self):
        self.assertEqual(self.fridge.cull_drinks(), 1)
        self.stock_indices = [[0, 2, 4], [3]]
        self.testStockingAndCheckSameDrinks()

    def testAgeAndCullDrinks(self):
        self.fridge.age_drinks()
        self.fridge.cull_drinks()
        self.stock_indices = [[0, 4], [3]]
        self.testStockingAndCheckSameDrinks()

    def testAgeTwiceAndCullDrinks(self):
        self.fridge.age_drinks()
        self.fridge.age_drinks()
        self.fridge.cull_drinks()
        self.stock_indices = [[4], [3]]
        self.testStockingAndCheckSameDrinks()


class RefrigeratorMultistockTests(RefrigeratorStockTests):
    """Stock refrigerator multiple times, with aging and culling"""
    def setUp(self):
        capacities = [1, 2, 3]
        self.fridge = Refrigerator(capacities)
        self.drinks = [Drink("a", 0), Drink("b", 2), Drink("c", 3),
                       Drink("d", 4), Drink("e", 1)]
        self.drinks_cpy = self.drinks[:]
        self.stock_indices = [[0], [1, 3], [2, 4]]
        self.safe_stock(copy_drinks=False)

    def testStockDoesntModifyDrinks(self):
        self.assertEqual(self.drinks, self.drinks_cpy)

    def testStockMore(self):
        # Try stocking a second time
        old_drinks = self.drinks
        self.drinks = [Drink("f", 6)]
        self.safe_stock()
        self.drinks = old_drinks + self.drinks
        self.stock_indices = [[0], [1, 3], [2, 4, 5]]
        self.testStockingAndCheckSameDrinks()

    def testRestockWithAgeAndCull(self):
        # Age and stock with another drink
        self.fridge.age_drinks()
        old_drinks = self.drinks
        self.drinks = [Drink("f", 6)]
        self.safe_stock()
        old_drinks.extend(self.drinks)
        # Age, cull, and stock with more
        self.fridge.age_drinks()
        self.fridge.cull_drinks()
        self.drinks = [Drink("g", 2), Drink("h", 3)]
        self.safe_stock()
        self.drinks = old_drinks + self.drinks
        self.stock_indices = [[6], [1, 3], [2, 5, 7]]
        self.testStockingAndCheckSameDrinks()


class CustomerSharedTests(unittest.TestCase):
    def setUp(self):
        from convenience import SimpleCustomer
        self.customer = SimpleCustomer()

    def safe_stock(self, fridge, drinks):
        fridge.stock_drinks(drinks[:])

    def testZeroCapacityFridge(self):
        """Testing get_drink on zero capacity refrigerator."""
        fridge = Refrigerator([])
        self.assertEqual(self.customer.get_drink(fridge), None)

        fridge = Refrigerator([0])
        self.assertEqual(self.customer.get_drink(fridge), None)

        fridge = Refrigerator([0, 0, 0])
        self.assertEqual(self.customer.get_drink(fridge), None)

    def testEmptyFridge(self):
        """Test on empty fridge with capacity"""
        fridge = Refrigerator([1])
        self.assertEqual(self.customer.get_drink(fridge), None)

        fridge = Refrigerator([0, 1, 0])
        self.assertEqual(self.customer.get_drink(fridge), None)

    def testOneDrinkSimple(self):
        """Testing get_drink on simple 1 drink fridge."""
        drinks = [Drink('pepsi', 1)]
        fridge = Refrigerator([2])
        self.safe_stock(fridge, drinks)
        self.assertEqual(self.customer.get_drink(fridge), drinks[0])

    def testOneDrinkHard(self):
        """Testing get_drink on harder 1 drink fridge."""
        drinks = [Drink('pepsi', 1)]
        fridge = Refrigerator([0, 0, 0, 0, 1])
        self.safe_stock(fridge, drinks)
        self.assertEqual(self.customer.get_drink(fridge), drinks[0])

    def testOneDrinkExpired(self):
        """Testing get_drink on expired 1 drink fridge."""
        drinks = [Drink('pepsi', -1)]
        fridge = Refrigerator([1])
        self.safe_stock(fridge, drinks)
        self.assertEqual(self.customer.get_drink(fridge), drinks[0])


    def testGetAll(self):
        """Testing get_drink until fridge empty."""
        drinks = [Drink('pepsi', 1), Drink('coke', 2), Drink('7-up', 7),
                  Drink("oj", -3)]
        fridge = Refrigerator([0, 1, 3])
        self.safe_stock(fridge, drinks)

        # Get drinks until fridge is empty (order ignored)
        for i in range(len(drinks)):
            drink = self.customer.get_drink(fridge)
            self.assertIn(drink, drinks)
            drinks.remove(drink)

        # Make sure all drinks were gotten
        self.assertEquals(drinks, [])

        # Make sure getting another drink returns None
        self.assertEquals(self.customer.get_drink(fridge), None)


# Test SimpleCustomer class:
class SimpleCustomerTests(CustomerSharedTests):
    def setUp(self):
        from convenience import SimpleCustomer
        self.customer = SimpleCustomer()

    def testFullMultiDrink(self):
        """Testing get_drink on normal, mostly-filled fridge."""
        drinks = [Drink('pepsi', 1), Drink('coke', 2), Drink('7-up', 7),
                  Drink('dr pepper', 42)]
        fridge = Refrigerator([1, 3, 1])
        self.safe_stock(fridge, drinks)

        # 1st SimpleCustomer: simple case, pick first drink on first shelf
        self.assertEqual(self.customer.get_drink(fridge), drinks[0])

        # 2nd SimpleCustomer: Empty Shelf case
        # first shelf empty, pick first on 2nd shelf
        self.assertEqual(self.customer.get_drink(fridge), drinks[1])

        # 3rd SimpleCustomer: Empty Shelf case, same as 2nd customer
        self.assertEqual(self.customer.get_drink(fridge), drinks[3])

        # 4th SimpleCustomer: 2 Empty Shelves, pick on 3rd shelf
        self.assertEqual(self.customer.get_drink(fridge), drinks[2])

        # 5th SimpleCustomer: Empty refrigerator case, return None
        self.assertEqual(self.customer.get_drink(fridge), None)


# Test AmbivalentCustomer class:
class AmbivalentCustomerTests(CustomerSharedTests):
    def setUp(self):
        from convenience import AmbivalentCustomer

        self.customer = AmbivalentCustomer()

    def testGetDrink(self):
        """Testing get_drink on multiple drinks."""
        drinks = [Drink('pepsi', 5), Drink('coke', 5), Drink('7-up', 5),
                  Drink('NA', 1), Drink('NA', 1), Drink('NA', 1)]

        count = {0: 0, 1: 0, 2: 0}
        n_times = 1000
        for i in xrange(n_times):
            fridge = Refrigerator([2, 2, 2])
            self.safe_stock(fridge, drinks)
            drink = self.customer.get_drink(fridge)
            count[drinks.index(drink)] += 1

        for n in count.values():
            self.assertTrue(280 < n < 400, "Expected count in range [280, 400]"
                            " but found %r" % n)


# Test DeterminedCustomer class:
class DeterminedCustomerTests(CustomerSharedTests):
    def setUp(self):
        from convenience import DeterminedCustomer

        self.customer = DeterminedCustomer()

    def testSimpleGetDrink(self):
        """Testing get_drink on multiple drinks."""
        # set up fridge
        fridge = Refrigerator([1, 1, 1])
        drinks = [Drink('pepsi', 7), Drink('milk', 1), Drink('7-up', 5)]
        self.safe_stock(fridge, drinks)

        self.assertEqual(self.customer.get_drink(fridge), drinks[0])
        self.assertEqual(no_whitespace(str(fridge)), \
no_whitespace("""shelf 0: [back]  [front]
shelf 1: [back] milk (1 day(s) until expiry) [front]
shelf 2: [back] 7-up (5 day(s) until expiry) [front]"""))

    def testMoveSkipGetDrink(self):
        """Testing get_drink on multiple drinks."""
        # set up fridge
        fridge = Refrigerator([1, 1, 1])
        drinks = [Drink('pepsi', 3), Drink('milk', 1), Drink('7-up', 5)]
        self.safe_stock(fridge, drinks)

        self.assertEqual(self.customer.get_drink(fridge), drinks[2])
        self.assertEqual(no_whitespace(str(fridge)), \
no_whitespace("""shelf 0: [back]  [front]
shelf 1: [back] milk (1 day(s) until expiry) [front]
shelf 2: [back] pepsi (3 day(s) until expiry) [front]"""))


    def testMoveGetDrink(self):
        """Testing get_drink on multiple drinks."""
        # set up fridge
        fridge = Refrigerator([1, 1, 1])
        drinks = [Drink('milk', 1), Drink('pepsi', 3), Drink('7-up', 5)]
        self.safe_stock(fridge, drinks)

        self.assertEqual(self.customer.get_drink(fridge), drinks[2])
        self.assertEqual(no_whitespace(str(fridge)), \
no_whitespace("""shelf 0: [back]  [front]
shelf 1: [back] milk (1 day(s) until expiry) [front]
shelf 2: [back] pepsi (3 day(s) until expiry) [front]"""))


    def testStrictlyEarlierGetDrink(self):
        """Testing get_drink on multiple drinks."""
        # set up fridge
        fridge = Refrigerator([1, 1, 1])
        drinks = [Drink('milk', 1), Drink('pepsi', 5), Drink('7-up', 5)]
        self.safe_stock(fridge, drinks)

        self.assertEqual(self.customer.get_drink(fridge), drinks[1])
        self.assertEqual(no_whitespace(str(fridge)), \
no_whitespace("""shelf 0: [back]  [front]
shelf 1: [back] milk (1 day(s) until expiry) [front]
shelf 2: [back] 7-up (5 day(s) until expiry) [front]"""))

        self.assertEqual(self.customer.get_drink(fridge), drinks[2])
        self.assertEqual(no_whitespace(str(fridge)), \
no_whitespace("""shelf 0: [back]  [front]
shelf 1: [back]  [front]
shelf 2: [back] milk (1 day(s) until expiry) [front]"""))


if __name__ == '__main__':
    unittest.main()
