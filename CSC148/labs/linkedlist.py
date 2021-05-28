
class Node(object):
    """A Linked-list node

    Instance variables:
    data: data for the current node
    next: the next node in the list, or None if terminal node
    """
    # We discussed why it's alright to have the data and next
    # not start with an underscore ("_") here.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

if __name__ == "__main__":
    b = Node(3)
    a = Node(5, next=b)

    print "a:", a
    print "a.data:", a.data
    print "a.next:", a.next
    print "a.next.data:", a.next.data
    print "a.next.next:", a.next.next

    # How do we loop over the list?
    print "Looping over a linked list:"
    node = a
    while node is not None:
        print node.data
        node = node.next


class Stack(object):
    """A stack of objects"""
    # We'll implement this with a linked list
    def __init__(self):
        # Head of linked list
        self._head = None

    def push(self, e):
        """(Stack, object) -> NoneType
        Push e onto the top of the stack
        """
        # put e at the head of the linked list
        node = Node(e, next=self._head)
        # Make self._head point to new beginning of list
        self._head = node

        # Could also do the following, as long we we defined the Node's
        # __init__ method to be able to take a "next" argument:
        # self._head = Node(e, next=self._head)

    def pop(self):
        """Stack -> object
        Remove and return the top element on the stack
        """
        # pop the element at the head of the linked list
        # Gets data from first node
        data = self._head.data
        # Remove first node
        self._head = self._head.next
        return data

    def is_empty(self):
        """Stack -> bool
        Return whether or not the stack is empty
        """
        # This is worse style: "return self._head == None"
        return self._head is None


if __name__ == "__main__":
    deck = Stack()
    deck.push("ace of spades")
    deck.push("two of diamonds")

    assert deck.pop() == "two of diamonds"
    assert deck.pop() == "ace of spades"