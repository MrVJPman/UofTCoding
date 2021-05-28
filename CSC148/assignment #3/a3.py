
import sys
import struct  # for binary file processing

from binary import iter_bytes
from huffman import HuffmanCoder

def encode(code_filename, input_filename, output_filename):
    # Parse code file into dictionary
    huffman_code = {}
    with open(code_filename) as ifp:
        for line in ifp:
            byte, code = line.strip().split(": ")
            huffman_code[int(byte)] = code

    # Convert input file to list of binary code strings
    bits = []
    with open(input_filename, "rb") as ifp:
        for byte in iter_bytes(ifp):
            code = huffman_code[byte]
            bits.append(code)

    # Add pseudo-eof and a byte's worth of buffer
    bits.append(huffman_code[max(huffman_code)])
    bits.append("00000000")

    # Write bits in char_str, 8 at a time (whole bytes)
    char_str = ''.join(bits)
    with open(output_filename, "wb") as ofp:
        while char_str:
            byte = struct.pack("c", chr(int(char_str[:8], 2)))
            ofp.write(byte)
            char_str = char_str[8:]


if __name__ == '__main__':
    hc = HuffmanCoder()
    prefix = "!"
    input = "%s.txt" % prefix
    code = "%s.code" % prefix
    binary = "%s.bin" % prefix
    output = "%s_decoded.txt" % prefix

    print >>sys.stderr, "===== Encoding ====="
    print >>sys.stderr, "Generating code from %s" % input
    with open(input, "rb") as ifp:
        hc.create_code(ifp)
    
    print >>sys.stderr, "Writing code to %s" % code
    with open(code, "w") as ofp:
        hc.write_code(ofp)

    print >>sys.stderr, "Using %s to encode %s -> %s" % \
        (code, input, binary)
    encode(code, input, binary)

    print >>sys.stderr, "\n===== Decoding ====="
    hc = HuffmanCoder()
    print >>sys.stderr, "Reading code from %s" % code
    with open(code) as ifp:
        hc.read_code(ifp)

    print >>sys.stderr, "Decoding %s -> %s" % (binary, output)
    with open(binary, "rb") as ifp:
        with open(output, "wb") as ofp:
            hc.decode(ifp, ofp, 256)
