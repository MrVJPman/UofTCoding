import unittest
import radix

class TestRadixSort(unittest.TestCase):
    def test_empty(self):
        '''Test radix sort on an empty list.'''
        L = []
        radix.sort(L)
        # What can you assert here, if anything?
        self.assertEqual(L, [])

    def test_reverse(self):
        '''Test radix sort on an reverse sorted list.'''
        L = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        radix.sort(L)
        # What can you assert here, if anything?
        self.assertEqual(L, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        
    def test_reverse_negative(self):
        '''Test radix sort on an reverse sorted list.'''
        L = [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
        radix.sort(L)
        # What can you assert here, if anything?
        self.assertEqual(L, [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0])
        
    def test_reverse_negative_alternate(self):
        '''Test radix sort on an reverse sorted list.'''
        L = [0, -1, 2, -3, 4, -5, 6, -7, 8, -9]
        radix.sort(L)
        # What can you assert here, if anything?
        self.assertEqual(L, [-9, -7, -5, -3, -1, 0, 2, 4, 6, 8])

    def test_nearly_sorted(self):
        '''Test radix sort on an nearly sorted list.'''
        L = [1, 2, 3, 4, 5, 6, 7, 8, 0, 9]
        radix.sort(L)
        # What can you assert here, if anything?
        self.assertEqual(L, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        
    def test_nearly_sorted_negative(self):
        '''Test radix sort on an nearly sorted list.'''
        L = [-9, -8, -7, -6, -5, -4, -3, -2, 0, -1]
        radix.sort(L)
        # What can you assert here, if anything?
        self.assertEqual(L, [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0])
    
    def test_nearly_sorted_negative_alternate(self):
        '''Test radix sort on an nearly sorted list.'''
        L = [9, -8, 7, -6, 5, -4, 3, -2, 0, 1]
        radix.sort(L)
        # What can you assert here, if anything?
        self.assertEqual(L, [-8, -6, -4, -2, 0, 1, 3, 5, 7, 9])
        
    def test_random(self):
        '''Test radix sort on an random list.'''
        L = [0, 5, 2, 1, 4, 3, 8, 9, 7, 6]
        radix.sort(L)
        # What can you assert here, if anything?
        self.assertEqual(L, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        
    def test_random_negative(self):
        '''Test radix sort on an random list.'''
        L = [0, -5, -2, -1, -4, -3, -8, -9, -7, -6]
        radix.sort(L)
        # What can you assert here, if anything?
        self.assertEqual(L, [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0])

    def test_random_negative_alternate(self):
        '''Test radix sort on an random list.'''
        L = [0, 5, -2, 1, -4, 3, -8, 9, 7, -6]
        radix.sort(L)
        # What can you assert here, if anything?
        self.assertEqual(L, [-8, -6, -4, -2, 0, 1, 3, 5, 7, 9])    

    def test_high_powers_reverse(self):
        '''Test radix sort on an reverse sorted list with differenting powers.'''
        L = [100000000, 10000000, 1000000, 100000, 10000, 1000, 100, 10, 1]
        radix.sort(L)
        # What can you assert here, if anything?
        self.assertEqual(L, [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000])
        
    def test_high_powers_reverse_negative(self):
        '''Test radix sort on an reverse sorted list with differenting powers.'''
        L = [-100000000, -10000000, -1000000, -100000, -10000, -1000, -100, -10, -1]
        radix.sort(L)
        # What can you assert here, if anything?
        self.assertEqual(L, [-100000000, -10000000, -1000000, -100000, -10000, -1000, -100, -10, -1])

    def test_high_powers_reverse_negative_alternate(self):
        '''Test radix sort on an reverse sorted list with differenting powers.'''
        L = [-100000000, 10000000, -1000000, 100000, -10000, 1000, -100, 10, -1]
        radix.sort(L)
        # What can you assert here, if anything?
        self.assertEqual(L, [-100000000, -1000000, -10000, -100, -1, 10, 1000, 100000, 10000000])

    def test_high_powers_nearly_sorted(self):
        '''Test radix sort on an nearly sorted list with differenting powers.'''
        L = [10, 100, 1000, 10000, 100000, 1000000, 10000000, 1, 100000000]
        radix.sort(L)
        # What can you assert here, if anything?
        self.assertEqual(L, [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000])

    def test_high_powers_nearly_sorted_reversed(self):
        '''Test radix sort on an nearly sorted list with differenting powers.'''
        L = [-10, -100, -1000, -10000, -100000, -1000000, -10000000, -1, -100000000]
        radix.sort(L)
        # What can you assert here, if anything?
        self.assertEqual(L, [-100000000, -10000000, -1000000, -100000, -10000, -1000, -100, -10, -1])

    def test_high_powers_nearly_sorted_reversed_alternate(self):
        '''Test radix sort on an nearly sorted list with differenting powers.'''
        L = [-10, 100, -1000, 10000, -100000, 1000000, -10000000, 1, -100000000]
        radix.sort(L)
        # What can you assert here, if anything?
        self.assertEqual(L, [-100000000, -1000000, -10000, -100, -1, 10, 1000, 100000, 10000000])

    def test_high_powers_random(self):
        '''Test radix sort on a random list with differenting powers.'''
        L = [1, 100000, 100, 10, 10000, 1000, 100000000, 10000000, 1000000]
        radix.sort(L)
        # What can you assert here, if anything?
        self.assertEqual(L, [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000])

    def test_high_powers_random_reverse(self):
        '''Test radix sort on a random list with differenting powers.'''
        L = [-1, -100000, -100, -10, -10000, -1000, -100000000, -10000000, -1000000]
        radix.sort(L)
        # What can you assert here, if anything?
        self.assertEqual(L, [-100000000, -10000000, -1000000, -100000, -10000, -1000, -100, -10, -1])

    def test_high_powers_random_reverse_alternate(self):
        '''Test radix sort on a random list with differenting powers.'''
        L = [-1, 100000, -100, 10, -10000, 1000, -100000000, 10000000, -1000000]
        radix.sort(L)
        # What can you assert here, if anything?
        self.assertEqual(L, [-100000000, -10000000, -1000000, -100000, -10000, -1000, -100, -10, -1])    
    
    def test_base_case(self):
        '''Test radix sort on the base case given in the lab.'''
        L = [240, 28, 5, 18, 140, 2]
        radix.sort(L)
        # What can you assert here, if anything?
        self.assertEqual(L, [2, 5, 18, 28, 140, 240])
        
    def test_base_negative_case(self):
        '''Test radix sort on the base case given in the lab.'''
        L = [240, -28, 5, -18, 140, -2]
        radix.sort(L)
        # What can you assert here, if anything?
        self.assertEqual(L, [-28, -18, -2, 5, 140, 240])

if __name__ == '__main__':
    unittest.main()
