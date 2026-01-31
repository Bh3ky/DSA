"""
PROBLEM: Implement run-length encoding and decoding functions. Assume the string
to be encoded consisting of letters of the alphabet, with no digits, and the string
to be decoded is a valid encoding.
"""

class Solution(object):
    def encode(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        
        result = []
        count = 1

        for i in range(1, len(s) + 1):
            # if same character, then we increase the count
            if i < len(s) and s[i] == s[i - 1]:
                count += 1
            else:
                # character changed or end of string
                result.append(str(count) + s[i - 1])
                count = 1

        return "".join(result)
    
    def decode(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        count = 0

        for j in s:
            if j.isdigit():
                # build multi-digit number
                count = count * 10 + int(j)
            else:
                # j is a letter
                result.append(j * count) # repeat the letter count times 
                count = 0 # reset count

        return "".join(result)