
def iter_bytes(file):
    """binary file reader -> iter(bytes as ints)
    Return an interator over the bytes in a binary file reader such that
    the following will iterate over each byte as an int in the file:

    for byte in iter_bytes(file):
        # do something with byte
    """
    while True:
        # Read a byte at a type from the open input file
        byte = file.read(1)
        # Stop at the end of the file
        if not byte:
            break

        # Yield the integer value of the bytes
        yield ord(byte)

def iter_bits(file):
    """binary file reader -> iter(bits as ints)
    Return an interator over the bits in a binary file reader such that
    the following will iterate over the int 1s and 0s in file:

    for bit in iter_bits(file):
        # do something with bit
    """
    for byte in iter_bytes(file):
        # Convert the byte to eight bits
        bits = []
        for i in range(8):
            bits.append(byte % 2)
            byte /= 2
            
        # Reverse the order of the bits so the most significant bit is first
        bits.reverse()
        for bit in bits:
            yield bit
