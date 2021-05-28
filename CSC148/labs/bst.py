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


def _insert(root, value):
    """Insert value into the BST and return the root"""
    # Recursively check root, root.left, root.right
    if root is None:
        # If the BSTNode class is inside of the BST class, we
        # create a new node like so:
        return BST.BSTNode(value)
    elif value < root.value:
        # Insert int the left subtree
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


if __name__ == "__main__":
    bst = BST()
    bst.insert(45)
    bst.insert(20)
    bst.insert(10)
    bst.insert(80)
    bst.insert(25)
    # "in" and "not in" keywords use the __contains__ method
    assert 11 not in bst
    assert 25 in bst