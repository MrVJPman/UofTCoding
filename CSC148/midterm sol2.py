class Node(object):
    def __init__(self, v, L=None, R=None):
        self.value = v
        self.left = L
        self.right = R

root = Node('A', Node('B'))

def to_list(root):
    if root is not None:
        tree_list = []
        tree_list.append(root.value)
        for child in [root.left, root.right]:
            tree_list.append(to_list(child))
        return tree_list



class ExprTree(object):

    def __init__(self, v, left=None, right=None):
        self.value = v
        self.left = left
        self.right = right

    def evaluate(self):
        if self.right is None and self.left is None:
            return self.value
        else:
            left = self.left.evaluate()
            right = self.right.evaluate()
            if self.value == '*':
                return left * right
            elif self.value == '+':
                return left + right

    def __str__(self):
        return _str(self)

def _str(root):
    if root.right is None and root.left is None:
        return str(root.value)
    else:
        left = _str(root.left)
        right = _str(root.right)
        return ''.join(['(', left, root.value, right, ')'])

if __name__ == '__main__':
    leaf1 = ExprTree(1)
    leaf3 = ExprTree(3)
    leaf4 = ExprTree(4)
    leaf5 = ExprTree(5)
    i1 = ExprTree('*', leaf3, leaf4)
    i2 = ExprTree('+', leaf1, i1)
    expr = ExprTree('*', i2, leaf5)


    NUMBERS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
'eight', 'nine']

def to_words(number):
    if number < 10 :
        return NUMBERS[number]
    else:
        return to_words(number/10) + ' ' + to_words(number % 10)

print to_words(23561)