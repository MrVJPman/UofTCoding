import unittest

class Queue(object):
    """A basic queue class"""
    # Implemented with a linked list
    def __init__(self):
        self._head = None
        self._tail = None

    def enqueue(self, elt):
        """(Queue, object) -> NoneType
        Add the element to the end of the queue
        """
        node = LinkedListNode(elt)
        if self.is_empty():
            self._head = node
        else:
            self._tail.next = node

        self._tail = node

    def dequeue(self):
        """Queue -> object
        Remove and return the element at the front of the queue
        """
        if self.is_empty():
            raise EmptyQueueError()

        data = self._head.data
        self._head = self._head.next
        return data

    def is_empty(self):
        """Queue -> bool
        Return whether or not the queue is empty
        """
        return self._head is None

class TestQueueSorting(unittest.TestCase):
    def setUp(self):
        print "set up Q"
        self.queue = Queue()

    def tearDown(self):
        print "tear down Q"
        self.queue = None

    def test_one_pos(self):
        print "test with one positive number"
        self.queue.enqueue(1.5)
        abs_sorted_to_sorted(self.queue)
        self.assertEqual(self.queue.dequeue(), -2530)

if __name__ == '__main__':
    def abs_sorted_to_sorted(queue):
        pass
    unittest.main()