class EmptyQueueError(Exception):
    pass


class LinkedListNode(object):
    def __init__(self, data, priority, next=None):
        """(LinkedListNode, object, float, LinkedListNode) -> NoneType"""
        self.data = data
        self.priority = priority
        self.next = next


class PriorityQueue(object):
    """A basic priority queue class"""
    # Implemented with a linked list
    def __init__(self):
        self._head = None

    def enqueue(self, elt, priority):
        """(Queue, object, float) -> NoneType
        Add the element to queue
        """
        new_node = LinkedListNode(elt, priority)
        if self.is_empty() or self._head.priority > priority:
            # Add the new node to the beginnning of the linked list
            new_node.next = self._head
            self._head = new_node
        else:
            # Add the new node to the appropriate point in the list
            # to preserve sorted order
            prev = None
            node = self._head
            while node is not None:
                if node.priority > priority:
                    break
                prev = node
                node = node.next

            # At this point, prev will point to the node before where we
            # want to insert new_node.
            # node might be None though, if we have to add to the end.
            new_node.next = prev.next
            prev.next = new_node
        
    def dequeue(self):
        """Queue -> object
        Remove and return the element with the lowest priority in the queue
        If multiple elements have the same priority, return the one that was
        added first to the queue.
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
    q = PriorityQueue()
    assert q.is_empty()
    values = [(1, "a"), (0, "b"), (5, "c"), (3, "d")]
    for priority, data in values:
        assert q.enqueue(data, priority) is None
        assert not q.is_empty()

    for priority, data in sorted(values):
        assert q.dequeue() == data

    assert q.is_empty()
    
    
