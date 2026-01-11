"""
PROBLEM: Design a program that takes as input a size k, and reads packets, continuously maintaining a
uniform random subset of size k of the read packets.

Hint: Suppose you have a procedure which selects k packets from the first n > k packets as specified. How
would you deal with the (n + 1)th packet?
"""

import random
import itertools

# method: reservior sampling (the algorithm)

def online_random_sample(it, k):
    # store first k elements
    sampling_results = list(itertools.islice(it, k))
    num_seen_so_far = k

    for x in it:
        num_seen_so_far += 1
        idx_to_replace = random.randrange(num_seen_so_far)
        if idx_to_replace < k:
            sampling_results[idx_to_replace] = x

    return sampling_results



# brute force approach would be to store all the packets read so far. after reading
# in each packet we apply solution on the preceding page to compute random subset of
# k packets. space complexity is high O(n) after n packets have been read.
# time complexity is also high O(nk). 