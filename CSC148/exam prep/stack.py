class Stack(object):
    '''A last-in, first-out (LIFO) stack of items.'''

    def __init__(self):
        '''(Stack) -> NoneType
        A new empty Stack.'''
        self._stack = []

    def push(self, v):
        '''(Stack, object) -> NoneType
        Make v the new top object on this stack.'''
        self._stack.append(v)

    # Another name for push.
    insert = push
    
    def pop(self):
        '''(Stack) -> object
        Remove and return the top item on this Stack.'''
        return self._stack.pop()

    # Another name for pop.
    remove = pop

    def top(self):
        '''(Stack) -> object
        Return the top item on this Stack.'''
        return self._stack[-1]
    
    # Another name for top.
    next_item = top

    def is_empty(self):
        '''(Stack) -> bool
        Return whether this Stack is empty.'''
        return not self._stack

    def size(self):
        '''(Stack) -> int
        Return the number of items in this Stack.'''
        return len(self._stack)


if __name__ == '__main__':
    stk = Stack()
    stk.push('a')
    stk.push('b')
    assert stk.size() == 2
    assert stk.top() == 'b'
    assert stk.pop() == 'b'
    assert stk.pop() == 'a'
    assert stk.is_empty()
    assert stk.size() == 0

    stk = Stack()
    stk.insert('a')
    stk.insert('b')
    assert stk.size() == 2
    assert stk.next_item() == 'b'
    assert stk.remove() == 'b'
    assert stk.remove() == 'a'
    assert stk.is_empty()
    assert stk.size() == 0
