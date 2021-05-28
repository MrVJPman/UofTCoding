def write_binary(n):
    """int -> NoneType
    print the binary representation of n to stdout

    e.g. 13,243 -> ???

    n % 2 -> last digit in binary
    n / 2
    """
    if n < 2:
        print n,
    else:
        # First print more-significant digit
        write_binary(int(n / 2)),
        print n % 2,


if __name__ == "__main__":
    write_binary(7)  # 111
    print ""
    write_binary(8)  # 1000
    print ""
    write_binary(13243)