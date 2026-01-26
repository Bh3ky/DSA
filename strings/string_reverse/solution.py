"""
PROBLEM: Implement a function for reversing the words in a string s.
"""

# note: we assume the string is encoded by bytearray

class Solution():
    def reverse_words(self, s: bytearray) -> None:

        # helper function to reverse characters in a given range
        def reverse_range(s, start, end):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
        
        # reverse the entire string
        reverse_range(s, 0, len(s) - 1)

        # reverse each word
        start = 0
        for i in range(len(s)):
            if s[i] == ord(' '): # space found
                reverse_range(s, start, i - 1)
                start = i + 1
                
        # reverse the last word
        reverse_range(s, start, len(s) - 1)

# time complexity O(n), since we spend O(1) per character where n is the lenth of s
# space complexity O(1)

