def BIT(n):
    """
    Returns a bit mask with the n-th bit set.
    Ex: BIT(3) -> 8 [100]
    """
    return 1 << n

def enable_bit(n, i):
    """
    Returns the number n with the i-th bit enabled
    """
    return n | BIT(i)

def disable_bit(n, i):
    """
    Returns the number n with the i-th bit disabled
    """
    return 0 if n == 0 else n & (BIT(i) ^ int('1'*n.bit_length(), 2))
