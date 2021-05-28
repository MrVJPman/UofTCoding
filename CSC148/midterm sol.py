class QueueTypeError(Exception):
    pass

class TypesafeQueue:
    def __init__(self, my_type):
        self.qtype = my_type
        self.queue = []
    def enqueue(self, o):
        if type(o) != self.qtype:
            raise QueueTypeError("should be %s, not %s" % (self.qtype, type(o)))
        self.queue.append(o)
    def dequeue(self):
        return self.queue.pop(0)

#import unittest


#class TestQueue(unittest.TestCase):
    #def testError(self):
        #self.queue = TypesafeQueue(str)
        #self.assertRaises(QueueTypeError, self.queue.enqueue, 1)

#unittest.main()

def add_all(q, L):
    for item in L:
        try:
            q.enqueue(item)
        except QueueTypeError:
            print item

que = TypesafeQueue(int)

add_all(que, [1,2,3,[],'str'])