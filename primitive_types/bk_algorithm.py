# Use of Brian Kernighan
def count_bits(n: int) -> int:
    count = 0
    while n:
        n &= n -1 # remove the lowest set bit
        count += 1
    return count