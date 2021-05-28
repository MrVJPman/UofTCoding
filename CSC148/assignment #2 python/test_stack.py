"""Test module Stack."""
"""modified, with thanks to Anya Tafliovich"""

import unittest
from stack import Stack, EmptyStackError

class StackEmptyTestCase(unittest.TestCase):
    """Test behaviour of an empty Stack."""

    def setUp(self):
        """Set up an empty stack."""
        self.stack = Stack()

    def tearDown(self):
        """Clean up."""
        self.stack = None

    def testIsEmpty(self):
        """Test is_empty() on empty Stack."""
        self.assertTrue(self.stack.is_empty(), \
                        'is_empty returned False on an empty Stack.')

    def testPush(self):
        """Test push to empty Stack."""
        self.stack.push("foo")
        self.assertEqual(self.stack.pop(), "foo", \
                         'Wrong item on top of the Stack: Expected "foo".')

    def testPop(self):
        self.assertRaises(EmptyStackError, self.stack.pop)


class StackAllTestCase(unittest.TestCase):
    """Tests of (non-empty) Stack."""

    def setUp(self):
        """Set up an empty stack."""
        self.stack = Stack()

    def tearDown(self):
        """Clean up."""
        self.stack = None

    def testAll(self):
        """Test pushing and popping multiple elements."""
        for item in range(20):
            self.stack.push(item)
            self.assertFalse(self.stack.is_empty(), \
                            'is_empty() returned True on a non-empty Stack.')

        expect = 19
        while not self.stack.is_empty():
            self.assertEqual(self.stack.pop(), expect,
                             'Something wrong on top of the Stack: Expected '
                             + str(expect) + '.')
            expect -= 1

if __name__ == '__main__':
    unittest.main()
