"""
You are given n numbers as well as probabilities po, p1,.-.,Pn-1, which sum up to 1. Given a random
number generator that produces values in [0,1] uniformly, how would you generate one of the 1
numbers according to the specified probabilities? For example, if the numbers are 3,5,7,11, and
the probabilities are 9/18,6/18,2/18, 1/18, then in 1000000 calls to your program, 3 should appear
roughly 500000 times, 5 should appear roughly 333333 times, 7 should appear roughly 111111 times,
and 11 should appear roughly 55555 times.

Hint: Look at the graph of the probability that the selected number is less than or equal to a. What do the
jumps correspond to?
"""

import random

def generate_nonuniform(values, probabilities):
    r = random.random() # uniform in [0, 1]
    cumulative = 0.0

    for value, prob in zip(values, probabilities):
        cumulative += prob
        if r < cumulative:
            return value 