from primitive_types.bit_counting import count_bits

def test_basic_cases():
    assert count_bits(12) == 2 # 1100
    assert count_bits(7) == 3 # 0111
    assert count_bits(255) == 8 # 11111111

def test_edge_cases():
    assert count_bits(0) == 0 # no 1 bits
    assert count_bits(1) == 1 # binary 1
    assert count_bits(2) == 1 # binary 10