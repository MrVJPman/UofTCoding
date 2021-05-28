class EmptyQueueError(Exception):
    pass


class LinkedListNode(object):
    def __init__(self, data, next=None):
        """(LinkedListNode, object, LinkedListNode) -> NoneType"""
        self.data = data
        self.next = next


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


if __name__ == "__main__":
    q = Queue()
    assert q.is_empty()
    values = ["a", "b", "c"]
    for val in values:
        assert q.enqueue(val) is None
        assert not q.is_empty()

    for val in values:
        assert q.dequeue() == val

    assert q.is_empty()
    
    
