from queue import Queue

class Node(object):
    """A node in a binary tree with a key and left and right children."""
    def __init__(self, k, left=None, right=None):
        """(Node, int) -> NoneType
        A Node with key k and left and right children.
        """
        self.key = k
        self.left = left
        self.right = right


def apply_by_level(root, fxn):
    q = Queue()
    q.enqueue(root)
    while not q.is_empty():
        node = q.dequeue()
        fxn(node.key)
        #for child in [node.left, node.right]:
        #    if child is not None:
        #        q.enqueue(child)

        if node.left is not None:
            q.enqueue(node.left)
        if node.right is not None:
            q.enqueue(node.right)

def make_tree(preorder, inorder):
    if len(preorder) == 0:
        return None
    else:
        key = preorder[0]
        index = inorder.index(key)
        left_inorder = inorder[:index]
        left_preorder = preorder[1:index + 1]
        right_inorder = inorder[index + 1:]
        right_preorder = preorder[index + 1:]
        return Node(key,
                    make_tree(left_preorder, left_inorder),
                    make_tree(right_preorder, right_inorder))

def print_(val):
    print val

if __name__ == '__main__':
    tree = Node(1, Node(2, Node(4), Node(5)), Node(3, None, Node(7)))
    apply_by_level(tree, print_)

    root = make_tree([10, 6, 8, 12, 11, 15], [8, 6, 12, 10, 11, 15])
    apply_by_level(root, print_)


