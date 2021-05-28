import StringIO
import huffman

StringIO.file1 = '''B'''

test_object=huffman.HuffmanCoder()
test_object.create_code(StringIO.file1)


def traverse_tree(root):
    if root.left is None and root.right is None:
        print root.key
    else:
        traverse_tree(root.left)
        traverse_tree(root.right)

