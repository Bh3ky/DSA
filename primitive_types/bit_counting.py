# counting the number of bits
def count_bits(x):
    num_bits = 0
    while x > 0:
        num_bits += x & 1 # check the lowest bit
        x >>= 1 # shift bits to the right
    return num_bits

# alternative method: improved performance
"""def count_bits_fast(x):
    num_bits = 0
    while x:
        x &= (x-1) # drops the lowest set bit
        num_bits += 1
    return num_bits
"""