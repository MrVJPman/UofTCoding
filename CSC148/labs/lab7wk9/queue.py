class Queue(object):

    def __init__(self):
        '''Make a new empty queue.'''
        self.queue = []
    
    def enqueue(self, o):
        '''Make o the new top item in this queue.'''
        self.queue.append(o)
        
    def dequeue(self):
        '''Remove and return the top item.'''
        return self.queue.pop(0)
    
    def front(self):
        '''Return the top item.'''
        return self.queue[0]
    
    def is_empty(self):
        '''Return whether there are any items in this queue.'''
        return self.queue == []
        
    def size(self):
        '''Return the number of items in this queue.'''
        return len(self.queue)
