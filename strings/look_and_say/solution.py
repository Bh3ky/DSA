"""
PROBLEM: Write a program that takes as input an integer n and returns the nth integer in the 
look-and-say sequence. Return the result as a string.
"""

class Solution:
    def look_and_say(self, n: int) -> str:
        # start of the sequence
        s = "1"

        # generate the sequence n - 1 times
        for _ in range(n - 1):
            s = self._next_number(s)

        return s

    def _next_number(self, s: str) -> str:
        result = []
        i = 0

        while i < len(s):
            count = 1

            # count consecutively identical digits
            while i + 1 < len(s) and s[i] == s[i + 1]:
                count += 1
                i += 1

            # append count and digit
            result.append(str(count) + s[i])
            i += 1

        return "".join(result)


# time complexity O(n · 2ⁿ): each iteration scans the full string
# and the length of the string can double each iteration (worst case)

# spce complexity O(2ⁿ): each iteration builds a new string
# note: space used is proportional to the string length.