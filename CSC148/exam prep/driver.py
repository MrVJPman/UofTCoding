'''A module for manipulating a binary search tree.'''

from node import Node
from queue import Queue
from stack import Stack

def insert(root, k):
    '''(Node, int) -> Node
    Insert k into the binary search tree rooted at root and return the root of
    the tree.
    Precondition: k is not already a key in the tree.
    '''
    if not root:
        return Node(k)
    else:
        # Find the node that will be the parent of the node containing k.
        r = root

        # TODO: modify this loop so that it find the correct Node to be the
        # parent of the Node containing k. You'll need to figure out whether
        # to move r left or right as you move down the tree.
        while (k < r.key and r.left is not None) or (k > r.key and r.right is not None):
            if k < r.key:
                r = r.left
            elif k < r.key:
                r = r.right



        # Once we get here (and thus the loop condition is false), r points to
        # the Node that will be the parent of the new Node for k. Create that new
        # Node and hang it off of the correct side of r.
        if k < r.key:
            r.left = Node(k)
        else:
            r.right = Node(k)

        return root

def contains(root, k):
    '''(Node, int) -> bool
    Return whether k is a key in the tree rooted at root.
    '''

    # TODO: complete this function without using recursion.
    pass

def print_tree(root):
    '''(Node) -> NoneType
    Print the tree rooted at root.'''

    _print_tree(root, '')

def _print_tree(root, indent):
    '''(Node, str) -> NoneType
    Print the tree rooted at root. Print indent (which consists only of
    whitespace) before the root value; indent more for the subtrees so that it
    looks nice.'''

    if root:
        _print_tree(root.right, indent + '   ')
        print indent + str(root.key)
        _print_tree(root.left, indent + '   ')


def print_value(v):
    '''(object) -> NoneType
    Print v without a newline.'''
    print v,

def traverse(root, func, container):
    '''(Node, function, Stack or Queue) -> NoneType
    Apply func to every key in the tree rooted at root, using container to store
    Nodes that we have encountered but not yet processed.'''

    pass

def inorder(root):
    '''(Node) -> NoneType
    Print the keys in the tree rooted at root in inorder order.'''

    pass

def postorder(root):
    '''(Node) -> NoneType
    Print the keys in the tree rooted at root in postorder order.'''

    pass

if __name__ == '__main__':
    # Put together the tree from the handout.
    root = insert(None, 8)
    root = insert(root, 4)
    root = insert(root, 9)
    root = insert(root, 1)
    root = insert(root, 6)
    print_tree(root)

    print '----------------'

    # What's in the tree?
    for i in range(10):
        print "%s is in the tree: %s." % (i, contains(root, i))

    print '----------------'

    stk = Stack()
    que = Queue()
    traverse(root, print_value, que)
    print
    traverse(root, print_value, stk)

    print '----------------'
    inorder(root)

    print '----------------'
    postorder(root)
