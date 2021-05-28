import unittest
from convenience import Drink, Refrigerator

class TwoDaysBeforeExpireDrinkCase(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Expired", 1)
    
    def testIsNotExpired(self):
        self.assertFalse(self.drink.is_expired(), \
                        'is_expired returned True on an non-expired Drink.')
    
    def testDaysBeforeExpire(self):
        self.assertEqual(self.drink.days_until_expiry(), 1, 'Not equal to 1 day')    
    
    def testAfterOneThenAnotherDay(self):
        self.drink.age_one_day()
        self.assertEqual(self.drink.days_until_expiry(), 0, 'Not equal to 0 day')
        self.assertFalse(self.drink.is_expired(), \
                        'is_expired returned True on non-expired Drink.')
        self.drink.age_one_day()
        self.assertEqual(self.drink.days_until_expiry(), -1, 'Not equal to -1 day')
        self.assertTrue(self.drink.is_expired(), \
                        'is_expired returned False on non-expired Drink.')


class OneDayBeforeExpireDrinkCase(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Not expired", 0)
    
    def testIsNotExpired(self):
        self.assertFalse(self.drink.is_expired(), \
                        'is_expired returned True on an non-expired Drink.')
        
    def testDaysBeforeExpire(self):
        self.assertEqual(self.drink.days_until_expiry(), 0, 'Not equal to 0 day')    
    
    def testExpiredAfterOneDay(self):
        self.drink.age_one_day()
        self.assertTrue(self.drink.is_expired(), \
                        'is_expired returned True on expired Drink.')

        
class ExpiredDrinkCase(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Expired", -1)
    
    def testIsExpired(self):
        self.assertTrue(self.drink.is_expired(), \
                        'is_expired returned False on an expired Drink.')

'''~~~~~~~~~~~~~~~~~~~~~~~~~Refrigerator TEST CASES~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

class IterLenStrTest(unittest.TestCase):
    def testZeroShelf(self):
        self.refrigerator = Refrigerator([])
        list_of_shelves = []
        for item in self.refrigerator:
            list_of_shelves.append(str(item))
            
        self.assertEqual(list_of_shelves, [] , "Got " + str(list_of_shelves) + " instead.")
        self.assertEqual(len(self.refrigerator), 0 , "Got " + str(len(self.refrigerator)) + " instead.")
        self.assertEqual(str(self.refrigerator), '' , "Got " + str(self.refrigerator) + " instead.")
            
        
    def testZeroCapacityNonZeroShelf(self):
        self.refrigerator = Refrigerator([0,0,0])
        list_of_shelves = []
        for item in self.refrigerator:
            list_of_shelves.append(str(item))
        
        self.assertEqual(list_of_shelves, ['[back]  [front]', '[back]  [front]', '[back]  [front]'] , "Got " + str(list_of_shelves) + " instead.")
        self.assertEqual(len(self.refrigerator), 3 , "Got " + str(len(self.refrigerator)) + " instead.")
        self.assertEqual(str(self.refrigerator), '[back]  [front]', '[back]  [front]', '[back]  [front]' , "Got " + str(self.refrigerator) + " instead.")
       
        
    def testNonZeroCapacityNonZeroShelf(self):
        self.refrigerator = Refrigerator([1,2,3])
        DrinkA = ("A", 1)
        DrinkB = ("B", 2)
        DrinkC = ("C", 3)
        DrinkD = ("D", 4)
        DrinkE = ("E", 5)
        DrinkF = ("F", 6)
        list_of_drinks = [DrinkA, DrinkB, DrinkC, DrinkD, DrinkE, DrinkF]
        for shelf in self.refrigerator:
            while not shelf.is_full():
                current_drink = list_of_drinks.pop(0)
                shelf.stock_drink(current_drink)
        list_of_shelves = []
        for item in self.refrigerator:
            list_of_shelves.append(item)
       

class Stock_DrinksTest(unittest.TestCase):
    def testZeroShelf(self):
        pass
   
    def testNonZeroCapacityNonZeroShelf(self):
        pass
    
    def testSomeFullCapacityNonZeroShelf(self):
        pass
    
class Age_DrinksAndCull_DrinksTest(unittest.TestCase):
    def testAge_Drinks(self):
        pass
    
    def testCullNoDrinks(self):
        pass

    def testCullSomeDrinks(self):
        pass
    
    def testCullAllDrinks(self):
        pass
   
if __name__ == '__main__':
    unittest.main()