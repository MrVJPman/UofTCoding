from binary import iter_bits, iter_bytes
from priority_queue import PriorityQueue


class UninitializedHuffmanCoderError(Exception):
    """An Exception, raised when a HuffmanCoder object does not contain a
    Huffman code(a binary tree)."""
    pass


class HuffmanCoder(object):
    """A Huffman coder, it is capable of creating a Huffman code from certain
    types of input file and also rewriting text or writing its Huffman code
    onto a file."""
    class HuffmanNode(object):
        """A HuffmanNode that is used in a Huffman binary tree. It is capable
        of having a key, a frequency and also up to two children which points
        to other HuffmanNodes."""
        def __init__(self, key=None, frequency=0, left=None, right=None):
            """HuffmanNode -> NoneType

            Initialize a HuffmanNode which automatically sets its key as None,
            frequency as 0, left as None, right as None if key, frequency,
            left, right agruments are not provided respectively.

            """
            self.key = key
            self.frequency = frequency
            self.left = left
            self.right = right

    def __init__(self):
        """HuffmanCoder -> NoneType

        Initialize a HuffmanCoder object with an initial empty Huffman binary
        tree.

        """
        self._Huffman_binary_tree = None

    def create_code(self, input_file):
        """(HuffmanCoder, binary file reader) -> NoneType

        Initialize the HuffmanCoder given a binary file reader containing
        the bytes to be compressed.

        """
        frequencies = [0] * 256
        for byte in iter_bytes(input_file):
            frequencies[byte] += 1
        self._create_code(frequencies)

    def _create_code(self, frequencies):
        """(HuffmanCoder, sequence(int)) -> NoneType

        Creates a Huffman binary tree inside the Huffman Coder object where the
        key of every HuffmanNode is the index of each non-zero integer in
        frequencies or None. For HuffmanNodes who's key contains said integers,
        its frequency will be the value(another integer) returned at index in
        frequencies. Else, when the key is None, the frequency instead will be
        equal to sum of the frequency of its child HuffmanNodes.

        """
        priority_queue_of_huffman_code = PriorityQueue()
        for ASCII_value in range(len(frequencies)):
            #Iterates over the frequency values, assigning index of the
            #sequences as the ASCII value.
            frequency_of_ASCII_value = frequencies[ASCII_value]
            if frequency_of_ASCII_value > 0:
                #If the frequency is greater than 0, create a Huffman code in
                #which the key is the ASCII_value(int), and frequency of the
                #node is the value returned at index ASCII_value. Then insert
                #them into a priority queue.
                ASCII_node = self.HuffmanNode(ASCII_value,
                                              frequency_of_ASCII_value)
                priority_queue_of_huffman_code.insert(ASCII_node,
                                                      frequency_of_ASCII_value)
        pseudo_eof_node = self.HuffmanNode(256, 1)
        priority_queue_of_huffman_code.insert(pseudo_eof_node, 1)
        #Creates the psuedo-eof note and insert them into the priority queue.
        while not len(priority_queue_of_huffman_code) == 1:
            #While there is more than one node in the priority queue. Keep on
            #building new internal nodes where its frequency is the sum of its
            #child node's frequencies. The resultant is a Huffman Code binary
            #tree once the priority queue has exactly one node.
            left_node = priority_queue_of_huffman_code.get_min()
            right_node = priority_queue_of_huffman_code.get_min()
            sum_of_child_frequency = left_node.frequency + right_node.frequency
            new_internal_node = self.HuffmanNode(None, sum_of_child_frequency,
                                        left_node, right_node)
            priority_queue_of_huffman_code.insert(new_internal_node,
                                                  sum_of_child_frequency)
        #Takes the one and last one item in the priority queue and assign it
        #as the Huffman code binary tree inside the HuffmanCoder object.
        self._Huffman_binary_tree = priority_queue_of_huffman_code.get_min()

    def write_code(self, file):
        """(HuffmanCoder, file writer) -> NoneType

        Writes the key-code information of HuffmanNodes of the Huffman binary
        tree inside the HuffmanCoder object and writes it to file. The
        Exception UninitializedHuffmanCoderError is raised if no Huffman binary
        tree exists within the HuffmanCoder Object.

        """
        if self._Huffman_binary_tree is None:
            raise UninitializedHuffmanCoderError('''HuffmanCoder does not
            contain a Huffman code. Initialize such code by using create_code()
            method or read_code() method.''')
        self._write(self._Huffman_binary_tree, '', file)

    def _write(self, root, code, output_file):
        """(HuffmanCoder, HuffmanNode, string, file writer) -> NoneType

        Traverses all of the child node in root that exists inside the
        HuffmanCoder object and writes 'int1: int2' on every new line where
        int1 is the key of root and int2 is code. Writing is only performed if
        key of the root exists(is not None.) and is done in traversal order.

        """
        if root.key is not None:
            #Check if key exists in the HuffmanNode, and if it does, write the
            #key, and code.
            output_file.writelines("%d: %s\n" % (root.key, code))
        else:
            #Else, if it doesn't, sets up the code for the the two child of
            #this node and recurse the writing procedure to the left and right
            #child of this node.
            left_code = ''.join([code, '0'])
            right_code = ''.join([code, '1'])
            self._write(root.left, left_code, output_file)
            self._write(root.right, right_code, output_file)

    def _insert(self, root, ASCII_value, binary_value):
        """(HuffmanCoder, HuffmanNode, string, file writer) -> NoneType

        Inserts ASCII_value in root(a Huffman code binary tree inside the
        HuffmanCoder object) at the proper position outlined by binary_value.
        Creates new Huffman Nodes as required.

        """
        if root is None:
            #Creates more nodes to expand the tree.
            root = self.HuffmanNode()
        if binary_value == '':
            #Place the ASCII as the node's key when binary_value is gone.
            root.key = int(ASCII_value)
        else:
            #Else, traverse to the left or right, changing binary_value.
            if binary_value[0] == '0':
                root.left = self._insert(root.left, ASCII_value,
                                         binary_value[1:])
            elif binary_value[0] == '1':
                root.right = self._insert(root.right, ASCII_value,
                                          binary_value[1:])
        #Return the CHANGE in the binary tree when done.
        return root

    def read_code(self, file):
        """(HuffmanCoder, file reader) -> NoneType

        Reads file and initialize a Huffman binary tree inside the HuffmanCoder
        object where the key of certain nodes and their code(position on the
        tree) is provided by file. Else, other nodes contain the default None
        as key.

        """
        line = file.readline().strip()
        #Cleans the file of new line space.
        while not line == '':
            #While not reached end of file, ASCII value and binary value is the
            #two string returned when spilting ': '. The ASCII value is then
            #written onto a huffman code binary tree, and its position based on
            #the value of binary_value. Then repeat with the next line.
            ASCII_value, binary_value = line.split(': ')
            line = file.readline().strip()
            self._Huffman_binary_tree = self._insert(self._Huffman_binary_tree,
                                                    ASCII_value, binary_value)

    def decode(self, input_file, output_file, eof):
        """(HuffmanCoder, binary file reader, binary file writer, int) ->
        NoneType

        Traverses the Huffman binary tree inside the HuffmanCoder object
        using the directions provided by input_file and write each reached
        key(a byte) as a character onto output_file. Traversal and writing is
        stopped when the reached key is same as eof. The Exception
        UninitializedHuffmanCoderError is raised if no Huffman binary tree
        exists within the HuffmanCoder Object.

        """
        if self._Huffman_binary_tree is None:
            raise UninitializedHuffmanCoderError('''HuffmanCoder does not
            contain a Huffman code. Initialize such code by using create_code()
            method or read_code() method.''')
        current_node = self._Huffman_binary_tree
        #Sets up the root of the tree initially as the current_node
        for bit in iter_bits(input_file):
            #Iterates overs the bits in input_file.
            if bit == 0:
                #Traverse left/right depending on value of the bit by replacing
                #the current traversal node as its left or right child.
                current_node = current_node.left
            elif bit == 1:
                current_node = current_node.right
            if current_node.key == eof:
                #Stops traversal once the node used for traversal has a key
                #equal to the eof
                break
            elif current_node.key is not None:
                #Else if the key is not empty(an int), writes the character
                #representation of the key onto the file. Then reset the
                #traversal by setting the root of the entire binary tree as the
                #current traversal node again.
                byte = current_node.key
                output_file.write(chr(byte))
                current_node = self._Huffman_binary_tree
