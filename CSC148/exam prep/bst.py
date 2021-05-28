class OMGDuplicateError(Exception):
    pass

class BST(object):
    class BSTNode(object):
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

    def __init__(self):
        self._root = None

    # Operations? insert, delete, is_empty?, __contains__

    # Treeprint op added by Velian
    def __str__(self):
        return _treeprint(self._root)
        
    def is_empty(self):
        return self._root is None

    def __contains__(self, value):
        """Return whether value is in the BST"""
        return _contains(self._root, value)

    def insert(self, value):
        """Insert value into the BST"""
        # No duplicates allowed
        if value in self:
            raise OMGDuplicateError("NO!")

        # The _insert method always returns the new root, so
        # always set self._root to what comes back.
        self._root = _insert(self._root, value)
    
    # written in class
    def delete(self, value):
        '''Delete value from the BST'''
        self._root = _delete(self._root, value)

def _insert(root, value):
    """Insert value into the BST and return the root"""
    # Recursively check root, root.left, root.right
    if root is None:
        # If the BSTNode class is inside of the BST class, we
        # create a new node like so:
        return BST.BSTNode(value)
    elif value < root.value:
        # Insert into the left subtree
        root.left = _insert(root.left, value)
    else:
        # Insert into the right subtree
        root.right = _insert(root.right, value)

    return root


def _contains(root, value):
    """Return whether value is in the BST rooted at root"""
    # Recursively check root, root.left, root.right
    if root is None:
        return False
    elif root.value == value:
        return True
    elif value < root.value:
        # Look at the left subtree
        return _contains(root.left, value)
    else:
        # Look at the right subtree
        return _contains(root.right, value)
        
        
# written in class
def _delete(node, val):
    '''(BSTNode, int) -> BSTNode
        Delete node with value val from tree rooted at node.
        Return new root of subtree (!!!)'''    
    
    if node is None:
        #reached a leaf, value not found
        return None
    elif val < node.value:
        node.left = _delete(node.left, val)
    elif val > node.value:
        node.right = _delete(node.right, val)
    else: # val == node.value
        # leaf
        if not node.left and not node.right:
            return None
        # one child
        elif not node.left:
            return node.right
        elif not node.right:
            return node.left
        # two children
        else:
            node.value = _largest(node.left)
            node.left = _delete(node.left, node.value)
    return node
        
# written in class
def _largest(node):
    '''(BSTNode) -> int
    Return the largest value in the tree rooted at node.
    Precondition: node is not None
    '''
    if not node.right:
        return node.value
    else:
        return _largest(node.right)
        

# Treeprint added by Velian
def _treeprint(node, num=0, acc=''):
    '''(BSTNode, int) -> NoneType
    Print a BST in a human-readable way with head cocked to the left'''

    if node is not None:
        acc += _treeprint(node.right, num + 1)
        acc += "\n"
        acc += "    " * num + str(node.value)
        acc += "\n"
        acc += _treeprint(node.left, num + 1)
    else:
        acc += "\n"
    return acc


if __name__ == "__main__":
    bst = BST()
    bst.insert(45)
    bst.insert(20)
    bst.insert(10)
    bst.insert(80)
    bst.insert(25)
    bst.insert(5)
    bst.insert(15)
    # "in" and "not in" keywords use the __contains__ method
    assert 11 not in bst
    assert 25 in bst
    print bst
    print "========"
    bst.delete(5)
    assert 5 not in bst
    print "========"
    print bst
    bst.delete(10)
    assert 10 not in bst
    print "========"
    print bst
    bst.delete(45)
    assert 45 not in bst
    print "========"
    print bst