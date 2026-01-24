"""
PROBLEM: Write a program which takes as input an array of characters,
and removes each ’b’ and replaces each ‘a’ by two ‘d’s. 
"""



class Solution:
    def replace_and_remove(self, s, size):
        # forward pass
        write_idx = 0
        a_count = 0

        for i in range(size):
            if s[i] != 'b':
                s[write_idx] = s[i]
                write_idx += 1
            if s[i] == 'a':
                a_count += 1

        # backward pass
        current_idx = write_idx - 1
        write_idx = write_idx + a_count - 1
        final_size = write_idx + 1

        while current_idx >= 0:
            if s[current_idx] == 'a':
                s[write_idx] = 'd'
                s[write_idx - 1] = 'd'
                write_idx -= 2
            else:
                s[write_idx] = s[current_idx]
                write_idx -= 1
            current_idx -= 1

        return final_size

# time complexity: forward pass O(n) and backward pass O(n)
# space complexity: in place and O(1)