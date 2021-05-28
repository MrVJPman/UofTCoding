class Queue(object):
    '''A first-in first-out (FIFO) data structure.'''

    def __init__(self):
        '''(Queue) -> NoneType
        Make a new empty queue.'''
        self._queue = []
    
    def enqueue(self, o):
        '''(Queue, object) -> NoneType
        Put o at the end of this queue.'''
        self._queue.append(o)

    # Another name for enqueue.
    insert = enqueue
        
    def front(self):
        '''(Queue) -> object
        Return the item that has been in this queue the longest.'''
        return self._queue[0]

    # Another name for front.
    next_item = front

    def dequeue(self):
        '''(Queue) -> object
        Remove and return the front item.'''
        return self._queue.pop(0)

    # Another name for dequeue.
    remove = dequeue
    
    def is_empty(self):
        '''(Queue) -> bool
        Return whether there are any items in this queue.'''
        return self._queue == []
        
    def size(self):
        '''(Queue) -> int
        Return the number of items in this queue.'''
        return len(self._queue)
        

if __name__ == '__main__':
    que = Queue()
    que.enqueue('a')
    que.enqueue('b')
    assert que.size() == 2
    assert que.front() == 'a'
    assert que.dequeue() == 'a'
    assert que.dequeue() == 'b'
    assert que.is_empty()
    assert que.size() == 0

    que = Queue()
    que.insert('a')
    que.insert('b')
    assert que.size() == 2
    assert que.next_item() == 'a'
    assert que.remove() == 'a'
    assert que.remove() == 'b'
    assert que.is_empty()
    assert que.size() == 0
