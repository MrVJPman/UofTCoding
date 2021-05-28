import unittest
from convenience import Drink, Refrigerator, SimpleCustomer,\
                        AmbivalentCustomer, DeterminedCustomer


def not_same_message(expected, produced):
    """ (anything, anything) -> str
    Return a message stating what was expected in a unitTest and
    what was produced in the actual code in the same test only
    run if expected is not the same as produced.
    """
    return "Expected:\n%s\ngot:\n%s\ninstead." % (str(expected), str(produced))


class TestDrinkAllMethods(unittest.TestCase):
    """Tests the behaviour of all of the methods in Drink class."""
    def setUp(self):
        """Sets up two Drink objects, one expired and one not expired."""
        self.drink = Drink("A", 1)
        self.expired_drink = Drink("B", -1)

    def tearDown(self):
        """Clean up."""
        self.drink = None
        self.expired_drink = None

    def test__str__(self):
        """Test __str__ method on a Drink object."""
        expected_str = "A (1 day(s) until expiry)"
        self.assertEqual(expected_str, str(self.drink),
                         not_same_message(expected_str, self.drink))

    def testdays_until_expiry(self):
        """Test days_until_expiry() method on a Drink object."""
        days_left = self.drink.days_until_expiry()
        self.assertEqual(1, days_left, not_same_message(1, days_left))

    def testage_one_day(self):
        """Test age_one_day() method on a Drink object."""
        self.drink.age_one_day()
        days_left = self.drink.days_until_expiry()
        self.assertEqual(0, days_left, not_same_message(0, days_left))

    def testis_expired(self):
        """Test is_expired() method on both Drink objects."""
        self.assertFalse(self.drink.is_expired(),
                         not_same_message(False, self.drink.is_expired()))
        self.assertTrue(self.expired_drink.is_expired(),
                        not_same_message(True, self.drink.is_expired()))


class TestRefrigeratorIterLenStr(unittest.TestCase):
    """Tests the behaviour of all of the public methods in Drink class."""
    def setUp(self):
        """Sets up three Refrigerator objects, one with no shelf, one with
        a single shelf and one with more than a single shelf. The last two
        shelves are filled with drinks."""
        self.no_shelf_refrigerator = Refrigerator([])
        self.single_shelf_refrigerator = Refrigerator([3])
        self.multi_shelf_refrigerator = Refrigerator([3, 3, 3])
        drink_list_for_single_shelf = [Drink("A", 1),
                                       Drink("B", 2), Drink("C", 3)]
        drink_list_for_multi_shelf = [Drink("A", 1), Drink("B", 2),
                                      Drink("C", 3), Drink("D", 4),
                                      Drink("E", 5), Drink("F", 6),
                                      Drink("G", 7), Drink("H", 8),
                                      Drink("I", 9)]
        for shelf in self.single_shelf_refrigerator:
            while not shelf.is_full():
                shelf.stock_drink(drink_list_for_single_shelf.pop(0))
        for shelf in self.multi_shelf_refrigerator:
            while not shelf.is_full():
                shelf.stock_drink(drink_list_for_multi_shelf.pop(0))

    def tearDown(self):
        """Clean up."""
        self.no_shelf_refrigerator = None
        self.single_shelf_refrigerator = None
        self.multi_shelf_refrigerator = None

    def testZeroShelfCase(self):
        """Test __iter__, __len__, and __str__ method on zero shelf
        Refrigerator object."""
        iterable = False
        for shelf in self.no_shelf_refrigerator:
            iterable = True
        self.assertFalse(iterable, not_same_message(False, iterable))
        self.assertEqual(0, len(self.no_shelf_refrigerator),
                         not_same_message(0, len(self.no_shelf_refrigerator)))
        self.assertEqual('', str(self.no_shelf_refrigerator),
                         not_same_message('', self.no_shelf_refrigerator))

    def testSingleShelfCase(self):
        """Test __iter__, __len__, and __str__ method on a single shelf
        Refrigerator object."""
        list_of_shelf = []
        list_of_shelf_copy = []
        for shelf in self.single_shelf_refrigerator:
            list_of_shelf.append(shelf)
        for shelf in iter(self.single_shelf_refrigerator):
            list_of_shelf_copy.append(shelf)
        drink_str_list = [str(Drink("C", 3)),
                          str(Drink("B", 2)), str(Drink("A", 1))]
        expected_str = 'shelf 0: [back] %s [front]' % ", ".join(drink_str_list)
        self.assertTrue(list_of_shelf == list_of_shelf_copy,
                        not_same_message(True,
                                         list_of_shelf == list_of_shelf_copy))
        self.assertEqual(1, len(self.single_shelf_refrigerator),
                         not_same_message(1,
                                          len(self.single_shelf_refrigerator)))
        self.assertEqual(expected_str, str(self.single_shelf_refrigerator),
                         not_same_message(expected_str,
                                          self.single_shelf_refrigerator))

    def testMultiShelfCase(self):
        """Test __iter__, __len__, and__str__ method on a multi shelf
        Refrigerator object."""
        list_of_shelf = []
        list_of_shelf_copy = []
        for shelf in self.multi_shelf_refrigerator:
            list_of_shelf.append(shelf)
        for shelf in iter(self.multi_shelf_refrigerator):
            list_of_shelf_copy.append(shelf)
        expected_str = 'shelf 0: [back] %s [front]' % (str(Drink("C", 3))
                                                       + ", "
                                                       + str(Drink("B", 2))
                                                       + ", "
                                                       + str(Drink("A",
                                                                   1))) + '\n'
        expected_str += 'shelf 1: [back] %s [front]' % (str(Drink("F", 6))
                                                        + ", "
                                                        + str(Drink("E", 5))
                                                        + ", "
                                                        + str(Drink("D",
                                                                    4))) + '\n'
        expected_str += 'shelf 2: [back] %s [front]' % (str(Drink("I", 9))
                                                        + ", "
                                                        + str(Drink("H", 8))
                                                        + ", " + str(Drink("G",
                                                                           7)))
        self.assertTrue(list_of_shelf == list_of_shelf_copy,
                        not_same_message(True,
                                         list_of_shelf == list_of_shelf_copy))
        self.assertEqual(3, len(self.multi_shelf_refrigerator),
                         not_same_message(3,
                                          len(self.single_shelf_refrigerator)))
        self.assertEqual(expected_str, str(self.multi_shelf_refrigerator),
                         not_same_message(expected_str,
                                          self.multi_shelf_refrigerator))


class TestRefrigeratorMethodstock_drinks(unittest.TestCase):
    """Tests the behaviour of stock_drink() method in Refrigerator."""
    def setUp(self):
        """Sets up three Refrigerator objects, one with a single shelf,
        one with more than a single shelf and one with more than a single
        shelf that contains a shelf with zero capacity."""
        self.single_shelf_refrigerator = Refrigerator([3])
        self.multi_shelf_refrigerator = Refrigerator([3, 3, 3])
        self.multi_shelf_refrigerator_single_zero_capacity = Refrigerator([3,
                                                                           0,
                                                                           3])

    def tearDown(self):
        """Clean up."""
        self.single_shelf_refrigerator = None
        self.multi_shelf_refrigerator = None
        self.multi_shelf_refrigerator_single_zero_capacity = None

    def testEmptySingleShelfCase(self):
        """Test stock_drinks() on an empty single shelf Refrigerator object."""
        drink_list = []
        index = 1
        for letter in "ABC":
            drink_list.append(Drink(letter, index))
            index += 1
        self.single_shelf_refrigerator.stock_drinks(drink_list)
        expected_str = 'shelf 0: [back] %s [front]' % (str(Drink("C", 3))
                                                       + ", "
                                                       + str(Drink("B", 2))
                                                       + ", " + str(Drink("A",
                                                                          1)))
        self.assertEqual(expected_str, str(self.single_shelf_refrigerator),
                         not_same_message(expected_str,
                                          self.single_shelf_refrigerator))

    def testNonEmptySingleShelfCase(self):
        """Test stock_drinks() on an non-empty single shelf Refrigerator
        object."""
        for shelf in self.single_shelf_refrigerator:
            shelf.put_drink(Drink('A', 1))
        drink_list = []
        index = 2
        for letter in "BC":
            drink_list.append(Drink(letter, index))
            index += 1
        self.single_shelf_refrigerator.stock_drinks(drink_list)
        expected_str = 'shelf 0: [back] %s [front]' % (str(Drink("C", 3))
                                                       + ", "
                                                       + str(Drink("B", 2))
                                                       + ", "
                                                       + str(Drink("A", 1)))
        self.assertEqual(expected_str, str(self.single_shelf_refrigerator),
                         not_same_message(expected_str,
                                          self.single_shelf_refrigerator))

    def testAllEmptyMultiShelfCase(self):
        """Test stock_drinks() on a Refrigerator object in which all of its
        shelves are empty."""
        drink_list = []
        index = 1
        for letter in "ABCDEFGHI":
            drink_list.append(Drink(letter, index))
            index += 1
        self.multi_shelf_refrigerator.stock_drinks(drink_list)
        expected_str = 'shelf 0: [back] %s [front]' % (str(Drink("G", 7))
                                                       + ", "
                                                       + str(Drink("D", 4))
                                                       + ", "
                                                       + str(Drink("A",
                                                                   1))) + '\n'
        expected_str += 'shelf 1: [back] %s [front]' % (str(Drink("H", 8))
                                                        + ", "
                                                        + str(Drink("E", 5))
                                                        + ", "
                                                        + str(Drink("B",
                                                                    2))) + '\n'
        expected_str += 'shelf 2: [back] %s [front]' % (str(Drink("I", 9))
                                                        + ", "
                                                        + str(Drink("F", 6))
                                                        + ", " + str(Drink("C",
                                                                           3)))
        self.assertEqual(expected_str, str(self.multi_shelf_refrigerator),
                         not_same_message(expected_str,
                                          self.multi_shelf_refrigerator))

    def testSingleNonEmptyMultiShelfCase(self):
        """Test stock_drinks() on a Refrigerator object in which there is one
        non-empty shelf."""
        list_of_initial_drinks_to_place = [Drink('A', 1)]
        for shelf in self.multi_shelf_refrigerator:
            while bool(list_of_initial_drinks_to_place):
                drink = list_of_initial_drinks_to_place.pop()
                shelf.stock_drink(drink)
        drink_list = []
        index = 2
        for letter in "BCDEFGHI":
            drink_list.append(Drink(letter, index))
            index += 1
        self.multi_shelf_refrigerator.stock_drinks(drink_list)
        expected_str = 'shelf 0: [back] %s [front]' % (str(Drink("E", 5))
                                                       + ", "
                                                       + str(Drink("B", 2))
                                                       + ", "
                                                       + str(Drink("A",
                                                                   1))) + '\n'
        expected_str += 'shelf 1: [back] %s [front]' % (str(Drink("H", 8))
                                                        + ", "
                                                        + str(Drink("F", 6))
                                                        + ", "
                                                        + str(Drink("C",
                                                                    3))) + '\n'
        expected_str += 'shelf 2: [back] %s [front]' % (str(Drink("I", 9))
                                                        + ", "
                                                        + str(Drink("G", 7))
                                                        + ", "
                                                        + str(Drink("D", 4)))
        self.assertEqual(expected_str, str(self.multi_shelf_refrigerator),
                         not_same_message(expected_str,
                                          self.multi_shelf_refrigerator))

    def testSingleFullShelfMultiShelfCase(self):
        """Test stock_drinks() on a Refrigerator object in which there is one
        shelf that's full."""
        list_of_initial_drinks_to_place = [Drink('A', 1), Drink('A', 1),
                                           Drink('A', 1)]
        shelf_index = 0
        for shelf in self.multi_shelf_refrigerator:
            while bool(list_of_initial_drinks_to_place) and shelf_index == 1:
                drink = list_of_initial_drinks_to_place.pop()
                shelf.stock_drink(drink)
            shelf_index += 1
        drink_list = []
        index = 2
        for letter in "ABCDEF":
            drink_list.append(Drink(letter, index))
            index += 1
        self.multi_shelf_refrigerator.stock_drinks(drink_list)
        expected_str = 'shelf 0: [back] %s [front]' % (str(Drink("E", 6))
                                                       + ", "
                                                       + str(Drink("C", 4))
                                                       + ", "
                                                       + str(Drink("A",
                                                                   2))) + '\n'
        expected_str += 'shelf 1: [back] %s [front]' % (str(Drink("A", 1))
                                                        + ", "
                                                        + str(Drink("A", 1))
                                                        + ", "
                                                        + str(Drink("A",
                                                                    1))) + '\n'
        expected_str += 'shelf 2: [back] %s [front]' % (str(Drink("F", 7))
                                                        + ", "
                                                        + str(Drink("D", 5))
                                                        + ", "
                                                        + str(Drink("B", 3)))
        self.assertEqual(expected_str, str(self.multi_shelf_refrigerator),
                         not_same_message(expected_str,
                                          self.multi_shelf_refrigerator))

    def testSingleZeroCapacityShelfMultiShelfCase(self):
        """Test stock_drinks() on a Refrigerator object in which there is one
        shelf with zero capacity."""
        drink_list = []
        index = 1
        for letter in "ABCDEF":
            drink_list.append(Drink(letter, index))
            index += 1
        self.multi_shelf_refrigerator_single_zero_capacity.\
            stock_drinks(drink_list)
        expected_str = 'shelf 0: [back] %s [front]' % (str(Drink("E", 5))
                                                       + ", "
                                                       + str(Drink("C", 3))
                                                       + ", "
                                                       + str(Drink("A",
                                                                   1))) + '\n'
        expected_str += 'shelf 1: [back]  [front]' + '\n'
        expected_str += 'shelf 2: [back] %s [front]' % (str(Drink("F", 6))
                                                        + ", "
                                                        + str(Drink("D", 4))
                                                        + ", "
                                                        + str(Drink("B", 2)))
        self.assertEqual(
            expected_str,
            str(self.multi_shelf_refrigerator_single_zero_capacity),
            not_same_message
            (expected_str, self.multi_shelf_refrigerator_single_zero_capacity))


class TestRefrigeratorMethod_age_drinks(unittest.TestCase):
    """Tests the behaviour of age_drinks() method in Refrigerator."""
    def setUp(self):
        """Sets up two Refrigerator objects, one with a single shelf and one
        with more than a single shelf. Both shelves are filled with drinks."""
        self.single_shelf_refrigerator = Refrigerator([3])
        self.multi_shelf_refrigerator = Refrigerator([3, 3, 3])
        drink_list_for_single_shelf = [Drink("A", 1), Drink("B", 2),
                                       Drink("C", 3)]
        drink_list_for_multi_shelf = [Drink("A", 1), Drink("B", 2),
                                      Drink("C", 3), Drink("D", 4),
                                      Drink("E", 5), Drink("F", 6),
                                      Drink("G", 7), Drink("H", 8),
                                      Drink("I", 9)]
        for shelf in self.single_shelf_refrigerator:
            while not shelf.is_full():
                shelf.stock_drink(drink_list_for_single_shelf.pop(0))
        for shelf in self.multi_shelf_refrigerator:
            while not shelf.is_full():
                shelf.stock_drink(drink_list_for_multi_shelf.pop(0))

    def tearDown(self):
        """Clean up."""
        self.single_shelf_refrigerator = None
        self.multi_shelf_refrigerator = None
        drink_list_for_single_shelf = None
        drink_list_for_multi_shelf = None

    def testSingleShelfCase(self):
        """Test age_drinks() on an single shelf Refrigerator object."""
        self.single_shelf_refrigerator.age_drinks()
        expected_str = 'shelf 0: [back] %s [front]' % (str(Drink("C", 2))
                                                       + ", "
                                                       + str(Drink("B", 1))
                                                       + ", "
                                                       + str(Drink("A", 0)))
        self.assertEqual(expected_str, str(self.single_shelf_refrigerator),
                         not_same_message(expected_str,
                                          self.single_shelf_refrigerator))

    def testMultiShelfCase(self):
        """Test age_drinks() on an multi shelf Refrigerator object."""
        expected_str = 'shelf 0: [back] %s [front]' % (str(Drink("C", 2))
                                                       + ", "
                                                       + str(Drink("B", 1))
                                                       + ", "
                                                       + str(Drink("A",
                                                                   0))) + '\n'
        expected_str += 'shelf 1: [back] %s [front]' % (str(Drink("F", 5))
                                                        + ", "
                                                        + str(Drink("E", 4))
                                                        + ", "
                                                        + str(Drink("D",
                                                                    3))) + '\n'
        expected_str += 'shelf 2: [back] %s [front]' % (str(Drink("I", 8))
                                                        + ", "
                                                        + str(Drink("H", 7))
                                                        + ", "
                                                        + str(Drink("G", 6)))
        self.multi_shelf_refrigerator.age_drinks()
        self.assertEqual(expected_str, str(self.multi_shelf_refrigerator),
                         not_same_message(expected_str,
                                          self.multi_shelf_refrigerator))


class TestRefrigeratorMethodcull_drinks(unittest.TestCase):
    """Tests the behaviour of cull_drinks() method in Refrigerator."""
    def setUp(self):
        """Sets up five Refrigerator objects, one with no shelf, four with more
        than a single shelf which only the Drink objects at the front, middle,
        back or all are removed. All five Refrigerator objects have drinks.
        """
        self.no_shelf_refrigerator = Refrigerator([])
        self.multi_shelf_refrigerator = Refrigerator([3, 3, 3])
        drink_list_for_multi_shelf = [Drink("A", 1), Drink("B", 2),
                                      Drink("C", 3), Drink("D", 4),
                                      Drink("E", 5), Drink("F", 6),
                                      Drink("G", 7), Drink("H", 8),
                                      Drink("I", 9)]
        for shelf in self.multi_shelf_refrigerator:
            while not shelf.is_full():
                shelf.stock_drink(drink_list_for_multi_shelf.pop(0))
        self.multi_shelf_refrigerator_front = Refrigerator([3, 3, 3])
        self.multi_shelf_refrigerator_mid = Refrigerator([3, 3, 3])
        self.multi_shelf_refrigerator_back = Refrigerator([3, 3, 3])
        drink_list_for_multi_shelf_only_front = [Drink("A", -1), Drink("B", 2),
                                                 Drink("C", 3), Drink("D", -1),
                                                 Drink("E", 5), Drink("F", 6),
                                                 Drink("G", -1), Drink("H", 8),
                                                 Drink("I", 9)]
        drink_list_for_multi_shelf_only_mid = [Drink("A", 1), Drink("B", -1),
                                               Drink("C", 3), Drink("D", 4),
                                               Drink("E", -1), Drink("F", 6),
                                               Drink("G", 7), Drink("H", -1),
                                               Drink("I", 9)]
        drink_list_for_multi_shelf_only_back = [Drink("A", 1), Drink("B", 2),
                                                Drink("C", -1), Drink("D", 4),
                                                Drink("E", 5), Drink("F", -1),
                                                Drink("G", 7), Drink("H", 8),
                                                Drink("I", -1)]
        for shelf in self.multi_shelf_refrigerator_front:
            while not shelf.is_full():
                shelf.stock_drink(drink_list_for_multi_shelf_only_front.pop(0))
        for shelf in self.multi_shelf_refrigerator_mid:
            while not shelf.is_full():
                shelf.stock_drink(drink_list_for_multi_shelf_only_mid.pop(0))
        for shelf in self.multi_shelf_refrigerator_back:
            while not shelf.is_full():
                shelf.stock_drink(drink_list_for_multi_shelf_only_back.pop(0))

    def tearDown(self):
        """Clean up."""
        self.no_shelf_refrigerator = None
        self.multi_shelf_refrigerator = None
        self.multi_shelf_refrigerator_front = None
        self.multi_shelf_refrigerator_mid = None
        self.multi_shelf_refrigerator_back = None
        drink_list_for_multi_shelf = None
        drink_list_for_multi_shelf_only_front = None
        drink_list_for_multi_shelf_only_mid = None
        drink_list_for_multi_shelf_only_back = None

    def testNoShelfCase(self):
        """Test cull_drinks() on an Refrigerator object without any shelves."""
        cull_drink_value = self.no_shelf_refrigerator.cull_drinks()
        self.assertEqual = (0, cull_drink_value,
                            not_same_message(0, cull_drink_value))

    def testNoneCulledMultiShelfCase(self):
        """Test cull_drinks() on an Refrigerator object with more than one
        shelf in which none of its drinks are expired."""
        cull_drink_value = self.multi_shelf_refrigerator.cull_drinks()
        self.assertEqual(0, cull_drink_value,
                         not_same_message(0, cull_drink_value))
        expected_str = 'shelf 0: [back] %s [front]' % (str(Drink("C", 3))
                                                       + ", "
                                                       + str(Drink("B", 2))
                                                       + ", "
                                                       + str(Drink("A",
                                                                   1))) + '\n'
        expected_str += 'shelf 1: [back] %s [front]' % (str(Drink("F", 6))
                                                        + ", "
                                                        + str(Drink("E", 5))
                                                        + ", "
                                                        + str(Drink("D",
                                                                    4))) + '\n'
        expected_str += 'shelf 2: [back] %s [front]' % (str(Drink("I", 9))
                                                        + ", "
                                                        + str(Drink("H", 8))
                                                        + ", "
                                                        + str(Drink("G", 7)))
        self.assertEqual(expected_str, str(self.multi_shelf_refrigerator),
                         not_same_message(expected_str,
                                          self.multi_shelf_refrigerator))

    def testAllCulledMultiShelfCase(self):
        """Test cull_drinks() on an Refrigerator object with more than one
        shelf in which all of its drinks are expired."""
        for index in range(10):
            self.multi_shelf_refrigerator.age_drinks()
        cull_drink_value = self.multi_shelf_refrigerator.cull_drinks()
        self.assertEqual(9, cull_drink_value,
                         not_same_message(9, cull_drink_value))
        expected_str = 'shelf 0: [back]  [front]' + '\n'
        expected_str += 'shelf 1: [back]  [front]' + '\n'
        expected_str += 'shelf 2: [back]  [front]'
        self.assertEqual(expected_str,
                         str(self.multi_shelf_refrigerator),
                         not_same_message(expected_str,
                                          self.multi_shelf_refrigerator))

    def testSomeCulledMultiShelfCase(self):
        """Test cull_drinks() on an Refrigerator object with more than one
        shelf in which some of its drinks are expired, existing in either at
        the front, middle, or back of all shelves."""
        front_culled_value = self.multi_shelf_refrigerator_front.cull_drinks()
        self.assertEqual(3, front_culled_value,
                         not_same_message(3, front_culled_value))
        expected_str = 'shelf 0: [back] %s [front]' % (str(Drink("C", 3))
                                                       + ", "
                                                       + str(Drink("B",
                                                                   2))) + '\n'
        expected_str += 'shelf 1: [back] %s [front]' % (str(Drink("F", 6))
                                                        + ", "
                                                        + str(Drink("E",
                                                                    5))) + '\n'
        expected_str += 'shelf 2: [back] %s [front]' % (str(Drink("I", 9))
                                                        + ", "
                                                        + str(Drink("H", 8)))
        self.assertEqual(expected_str,
                         str(self.multi_shelf_refrigerator_front),
                         not_same_message(expected_str,
                                          self.multi_shelf_refrigerator_front))
        mid_culled_value = self.multi_shelf_refrigerator_mid.cull_drinks()
        self.assertEqual(3, mid_culled_value,
                         not_same_message(3, mid_culled_value))
        expected_str = 'shelf 0: [back] %s [front]' % (str(Drink("C", 3))
                                                       + ", "
                                                       + str(Drink("A",
                                                                   1))) + '\n'
        expected_str += 'shelf 1: [back] %s [front]' % (str(Drink("F", 6))
                                                        + ", "
                                                        + str(Drink("D",
                                                                    4))) + '\n'
        expected_str += 'shelf 2: [back] %s [front]' % (str(Drink("I", 9))
                                                        + ", "
                                                        + str(Drink("G", 7)))
        self.assertEqual(expected_str,
                         str(self.multi_shelf_refrigerator_mid),
                         not_same_message(
                             expected_str,
                             self.multi_shelf_refrigerator_mid))
        back_culled_value = self.multi_shelf_refrigerator_back.cull_drinks()
        self.assertEqual(3, back_culled_value,
                         not_same_message(3, back_culled_value))
        expected_str = 'shelf 0: [back] %s [front]' % (str(Drink("B", 2))
                                                       + ", "
                                                       + str(Drink("A",
                                                                   1))) + '\n'
        expected_str += 'shelf 1: [back] %s [front]' % (str(Drink("E", 5))
                                                        + ", "
                                                        + str(Drink("D",
                                                                    4))) + '\n'
        expected_str += 'shelf 2: [back] %s [front]' % (str(Drink("H", 8))
                                                        + ", "
                                                        + str(Drink("G", 7)))
        self.assertEqual(expected_str,
                         str(self.multi_shelf_refrigerator_back),
                         not_same_message(
                             expected_str,
                             self.multi_shelf_refrigerator_back))


class TestSimpleCustomer(unittest.TestCase):
    """Tests the behaviour of get_drink() method in SimpleCustomer."""
    def setUp(self):
        """Sets up three Refrigerator objects, one without any shelves,
        one with more than a single shelf and one with more than a single
        shelf that contains a shelf with zero capacity. A SimpleCustomer
        object is also set up."""
        self.refrigerator = Refrigerator([3, 3, 3])
        self.refrigerator_empty = Refrigerator([])
        self.refrigerator_first_zero_capacity = Refrigerator([0, 3, 3])
        self.customer = SimpleCustomer()
        index = 1
        self.drink_list = []
        for letter in "ABCDEF":
            self.drink_list.append(Drink(letter, index))
            index += 1

    def tearDown(self):
        """Clean up."""
        self.refrigerator = None
        self.refrigerator_empty = None
        self.refrigerator_first_zero_capacity = None
        self.customer = None
        self.drink_list = None

    def testBaseCase(self):
        """Test get_drink() on a multi shelf Refrigerator object where all its
        shelves has some drink."""
        self.refrigerator.stock_drinks(self.drink_list)
        expected_str = 'A (1 day(s) until expiry)'
        obtained_drink = self.customer.get_drink(self.refrigerator)
        self.assertEqual(expected_str, str(obtained_drink),
                         not_same_message(expected_str, obtained_drink))

    def testFirstShelfEmptyCase(self):
        """Test get_drink() on a multi shelf Refrigerator object where its
        first shelf has no drinks."""
        self.refrigerator.stock_drinks(self.drink_list)
        passed_first_only = False
        for shelf in self.refrigerator:
            if not passed_first_only:
                while not shelf.is_empty():
                    shelf.take_drink()
            passed_first_only = True
        expected_str = 'B (2 day(s) until expiry)'
        obtained_drink = self.customer.get_drink(self.refrigerator)
        self.assertEqual(expected_str, str(obtained_drink),
                         not_same_message(expected_str, obtained_drink))

    def testFirstShelfZeroCapacityCase(self):
        """Test get_drink() on a multi shelf Refrigerator object where its
        first shelf has zero capacity."""
        self.refrigerator_first_zero_capacity.stock_drinks(self.drink_list)
        expected_str = 'A (1 day(s) until expiry)'
        obtained_drink = self.customer.get_drink(
            self.refrigerator_first_zero_capacity)
        self.assertEqual(expected_str, str(obtained_drink),
                         not_same_message(expected_str, obtained_drink))

    def testEmptyFridge(self):
        """Test get_drink() on two multi shelf Refrigerator object where both
        has no Drink objects. The first Refrigerator object have no Shelf
        objects while the second Refrigerator object has."""
        obtained_drink = self.customer.get_drink(self.refrigerator_empty)
        self.assertEqual(None, obtained_drink,
                         not_same_message(None, obtained_drink))
        obtained_drink = self.customer.get_drink(self.refrigerator)
        self.assertEqual(None, obtained_drink,
                         not_same_message(None, obtained_drink))


class TestAmbivalentCustomer(unittest.TestCase):
    """Tests the behaviour stock_drink() method in AmbivalentCustomer."""
    def setUp(self):
        """Sets up three Refrigerator objects, one without any shelves,
        one with more than a single shelf and one with more than a single
        shelf that contains only a shelf with non-zero capacity. An
        AmbivalentCustomer object is also set up."""
        self.refrigerator = Refrigerator([3, 3, 3, 3, 3])
        self.refrigerator_all_zero_but_one = Refrigerator([0, 10, 0])
        self.refrigerator_empty = Refrigerator([])
        self.customer = AmbivalentCustomer()
        index = 1
        self.drink_list = []
        for letter in "ABCDEFGHIJ":
            self.drink_list.append(Drink(letter, index))
            index += 1

    def tearDown(self):
        """Clean up."""
        self.refrigerator = None
        self.refrigerator_all_zero_but_one = None
        self.refrigerator_empty = None
        self.customer = None
        self.drink_list = None

    def testBaseCase(self):
        """Test get_drink() on a multi shelf Refrigerator object where all its
        shelves has some rinks"""
        self.refrigerator.stock_drinks(self.drink_list)
        expected_drinks = ['A (1 day(s) until expiry)',
                           'B (2 day(s) until expiry)',
                           'C (3 day(s) until expiry)',
                           'D (4 day(s) until expiry)',
                           'E (5 day(s) until expiry)']
        obtained_drink = self.customer.get_drink(self.refrigerator)
        self.assertTrue(str(obtained_drink) in expected_drinks,
                        not_same_message(True,
                                         str(obtained_drink) in
                                         expected_drinks))

    def testAllEmptyExceptOneCase(self):
        """Test get_drink() on a multi shelf Refrigerator object where all its
        shelves but one of its shelves has some drinks."""
        passed_first_only = False
        for shelf in self.refrigerator:
            if not passed_first_only:
                while not shelf.is_full():
                    shelf.stock_drink(self.drink_list.pop(0))
            passed_first_only = True
        expected_str = 'A (1 day(s) until expiry)'
        obtained_drink = self.customer.get_drink(self.refrigerator)
        self.assertEqual(expected_str, str(obtained_drink),
                         not_same_message(expected_str, obtained_drink))

    def testAllZeroCapacityExceptOneCase(self):
        """Test get_drink() on a multi shelf Refrigerator object all but a
        single shelf has non-zero capacity."""
        self.refrigerator_all_zero_but_one.stock_drinks(self.drink_list)
        expected_str = 'A (1 day(s) until expiry)'
        obtained_drink = self.customer.get_drink(
            self.refrigerator_all_zero_but_one)
        self.assertEqual(expected_str, str(obtained_drink),
                         not_same_message(expected_str, obtained_drink))

    def testEmptyFridge(self):
        """Test get_drink() on two multi shelf Refrigerator object where both
        has no Drink objects. The first Refrigerator object have no Shelf
        object while the second Refrigerator object has."""
        obtained_drink = self.customer.get_drink(self.refrigerator_empty)
        self.assertEqual(None, obtained_drink,
                         not_same_message(None, obtained_drink))
        obtained_drink = self.customer.get_drink(self.refrigerator)
        self.assertEqual(None, obtained_drink,
                         not_same_message(None, obtained_drink))


class TestDeterminedCustomer(unittest.TestCase):
    """Tests the behaviour of get_drink() method in DeterminedCustomer."""
    def setUp(self):
        """Sets up two Refrigerator objects, one without any shelves, and
        one with more than a single shelf. A DeterminedCustomer object is also
        set up."""
        self.refrigerator = Refrigerator([3, 3, 3, 3, 3])
        self.refrigerator_empty = Refrigerator([])
        self.customer = DeterminedCustomer()

    def tearDown(self):
        """Clean up."""
        self.refrigerator = None
        self.refrigerator_empty = None
        self.customer = None

    def testAlwaysIncreaseCase(self):
        """Test get_drink() on a multi shelf Refrigerator object where the
        frontmost Drink objects have increasing expiration date as the customer
        move pass the Shelf objects in the Refrigerator object."""
        drink_list = []
        index_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for letter in "ABCDEFGHIJ":
            drink_list.append(Drink(letter, index_list.pop(0)))
        self.refrigerator.stock_drinks(drink_list)
        expected_str = 'shelf 0: [back] %s [front]' % (str(Drink("F",
                                                                 6))) + '\n'
        expected_str += 'shelf 1: [back] %s [front]' % (str(Drink("G", 7))
                                                        + ", "
                                                        + str(Drink("A",
                                                                    1))) + '\n'
        expected_str += 'shelf 2: [back] %s [front]' % (str(Drink("H", 8))
                                                        + ", "
                                                        + str(Drink("B",
                                                                    2))) + '\n'
        expected_str += 'shelf 3: [back] %s [front]' % (str(Drink("I", 9))
                                                        + ", "
                                                        + str(Drink("C",
                                                                    3))) + '\n'
        expected_str += 'shelf 4: [back] %s [front]' % (str(Drink("J", 10))
                                                        + ", "
                                                        + str(Drink("D", 4)))
        obtained_drink = self.customer.get_drink(self.refrigerator)
        expected_drink = 'E (5 day(s) until expiry)'
        self.assertEqual(expected_drink, str(obtained_drink),
                         not_same_message(expected_drink, str(obtained_drink)))
        self.assertEqual(expected_str, str(self.refrigerator),
                         not_same_message(expected_str,
                                          str(self.refrigerator)))

    def testAlwaysDecrease(self):
        """Test get_drink() on a multi shelf Refrigerator object where the
        frontmost Drink objects have decreasing expiration date as the customer
        move pass the Shelf objects in the Refrigerator object."""
        drink_list = []
        index_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        for letter in "ABCDEFGHIJ":
            drink_list.append(Drink(letter, index_list.pop(0)))
        self.refrigerator.stock_drinks(drink_list)
        expected_str = 'shelf 0: [back] %s [front]' % (str(Drink("F",
                                                                 5))) + '\n'
        expected_str += 'shelf 1: [back] %s [front]' % (str(Drink("G", 4))
                                                        + ", "
                                                        + str(Drink("B",
                                                                    9))) + '\n'
        expected_str += 'shelf 2: [back] %s [front]' % (str(Drink("H", 3))
                                                        + ", "
                                                        + str(Drink("C",
                                                                    8))) + '\n'
        expected_str += 'shelf 3: [back] %s [front]' % (str(Drink("I", 2))
                                                        + ", "
                                                        + str(Drink("D",
                                                                    7))) + '\n'
        expected_str += 'shelf 4: [back] %s [front]' % (str(Drink("J", 1))
                                                        + ", "
                                                        + str(Drink("E", 6)))
        obtained_drink = self.customer.get_drink(self.refrigerator)
        expected_drink = 'A (10 day(s) until expiry)'
        self.assertEqual(expected_drink, str(obtained_drink),
                         not_same_message(expected_drink,
                                          str(obtained_drink)))
        self.assertEqual(expected_str, str(self.refrigerator),
                         not_same_message(expected_str,
                                          str(self.refrigerator)))

    def testNoChangeCase(self):
        """Test get_drink() on a multi shelf Refrigerator object where the
        frontmost Drink objects have no change in expiration date as the
        customer move pass the Shelf objects in the Refrigerator object.
        """
        drink_list = []
        index_list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        for letter in "ABCDEFGHIJ":
            drink_list.append(Drink(letter, index_list.pop(0)))
        self.refrigerator.stock_drinks(drink_list)
        expected_str = 'shelf 0: [back] %s [front]' % (str(Drink("F",
                                                                 1))) + '\n'
        expected_str += 'shelf 1: [back] %s [front]' % (str(Drink("G", 1))
                                                        + ", "
                                                        + str(Drink("B",
                                                                    1))) + '\n'
        expected_str += 'shelf 2: [back] %s [front]' % (str(Drink("H", 1))
                                                        + ", "
                                                        + str(Drink("C",
                                                                    1))) + '\n'
        expected_str += 'shelf 3: [back] %s [front]' % (str(Drink("I", 1))
                                                        + ", "
                                                        + str(Drink("D",
                                                                    1))) + '\n'
        expected_str += 'shelf 4: [back] %s [front]' % (str(Drink("J", 1))
                                                        + ", "
                                                        + str(Drink("E", 1)))
        obtained_drink = self.customer.get_drink(self.refrigerator)
        expected_drink = 'A (1 day(s) until expiry)'
        self.assertEqual(expected_drink, str(obtained_drink),
                         not_same_message(expected_drink, str(obtained_drink)))
        self.assertEqual(expected_str, str(self.refrigerator),
                         not_same_message(expected_str,
                                          str(self.refrigerator)))

    def testAlternatingIncreaseFirstDecreaseSecondCase(self):
        """Test get_drink() on a multi shelf Refrigerator object where the
        frontmost Drink objects has first increasing expiration date then
        decreasing expiration as the customer move pass the Shelf objects
        in the Refrigerator object."""
        drink_list = []
        index_list = [2, 4, 3, 5, 1, 1, 1, 1, 1, 1]
        for letter in "ABCDEFGHIJ":
            drink_list.append(Drink(letter, index_list.pop(0)))
        self.refrigerator.stock_drinks(drink_list)
        expected_str = 'shelf 0: [back] %s [front]' % (str(Drink("F",
                                                                 1))) + '\n'
        expected_str += 'shelf 1: [back] %s [front]' % (str(Drink("G", 1))
                                                        + ", "
                                                        + str(Drink("A",
                                                                    2))) + '\n'
        expected_str += 'shelf 2: [back] %s [front]' % (str(Drink("H", 1))
                                                        + ", "
                                                        + str(Drink("C",
                                                                    3))) + '\n'
        expected_str += 'shelf 3: [back] %s [front]' % (str(Drink("I", 1))
                                                        + ", "
                                                        + str(Drink("B",
                                                                    4))) + '\n'
        expected_str += 'shelf 4: [back] %s [front]' % (str(Drink("J", 1))
                                                        + ", "
                                                        + str(Drink("E", 1)))
        obtained_drink = self.customer.get_drink(self.refrigerator)
        expected_drink = 'D (5 day(s) until expiry)'
        self.assertEqual(expected_drink, str(obtained_drink),
                         not_same_message(expected_drink, str(obtained_drink)))
        self.assertEqual(expected_str, str(self.refrigerator),
                         not_same_message(expected_str,
                                          str(self.refrigerator)))

    def testAlternatingDecreaseFirstIncreaseSecondCase(self):
        """Test get_drink() on a multi shelf Refrigerator object where the
        frontmost Drink objects has first decreasing expiration date then
        increasing expiration as the customer move pass the Shelf objects
        in the Refrigerator object."""
        drink_list = []
        index_list = [3, 2, 4, 1, 5, 1, 1, 1, 1, 1]
        for letter in "ABCDEFGHIJ":
            drink_list.append(Drink(letter, index_list.pop(0)))
        self.refrigerator.stock_drinks(drink_list)
        expected_str = 'shelf 0: [back] %s [front]' % (str(Drink("F",
                                                                 1))) + '\n'
        expected_str += 'shelf 1: [back] %s [front]' % (str(Drink("G", 1))
                                                        + ", "
                                                        + str(Drink("B",
                                                                    2))) + '\n'
        expected_str += 'shelf 2: [back] %s [front]' % (str(Drink("H", 1))
                                                        + ", "
                                                        + str(Drink("A",
                                                                    3))) + '\n'
        expected_str += 'shelf 3: [back] %s [front]' % (str(Drink("I", 1))
                                                        + ", "
                                                        + str(Drink("D",
                                                                    1))) + '\n'
        expected_str += 'shelf 4: [back] %s [front]' % (str(Drink("J", 1))
                                                        + ", "
                                                        + str(Drink("C", 4)))
        obtained_drink = self.customer.get_drink(self.refrigerator)
        expected_drink = 'E (5 day(s) until expiry)'
        self.assertEqual(expected_drink, str(obtained_drink),
                         not_same_message(expected_drink, str(obtained_drink)))
        self.assertEqual(expected_str, str(self.refrigerator),
                         not_same_message(expected_str,
                                          str(self.refrigerator)))

    def testEmptyFridge(self):
        """Test get_drink() on two multi shelf Refrigerator object where both
        has no Drink objects. The first Refrigerator object have no Shelf
        object while the second Refrigerator object has."""
        obtained_drink = self.customer.get_drink(self.refrigerator_empty)
        self.assertEqual(None, obtained_drink,
                         not_same_message(None, obtained_drink))
        obtained_drink = self.customer.get_drink(self.refrigerator)
        self.assertEqual(None, obtained_drink,
                         not_same_message(None, obtained_drink))

if __name__ == '__main__':
    unittest.main()