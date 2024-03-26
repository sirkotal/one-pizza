def BIT(n):
    """
    Returns a bit mask with the n-th bit set.
    Ex: BIT(3) -> 8 [100]
    """
    return 1 << n

def flip_bits(n):
    """
    Flips all bits of a number.
    Ex: flip_bits(5) -> 2 [101 -> 010]
    """
    return n ^ int('1' * n.bit_length(), 2)
