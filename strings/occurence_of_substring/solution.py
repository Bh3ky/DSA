"""
PROBLEM: Given two strings s (the "search string") and t (the "text"), find 
the first occurence of s in t.
"""

class Solution(object):
    def strStr(self, t, s):
        """
        :type t: str
        :type s: str
        :rtype: int
        """

        # edge case
        if len(s) > len(t):
            return -1
        
        BASE = 26
        m = len(s)

        # compute hash for s and first window of t
        s_hash = 0
        t_hash = 0

        for i in range(m):
           s_hash = s_hash * BASE + (ord(s[i]) - ord('A'))
           t_hash = t_hash * BASE + (ord(t[i]) - ord('A'))

        # highest power of base used for removing left char
        power = BASE ** (m -1)

        # slide the window across t
        for i in range(m, len(t)):
            # check if hash matches then verify the strings
            if t_hash == s_hash and t[i - m:i] == s:
                return i - m
            
            # rolling hash update
            t_hash -= (ord(t[i - m]) - ord('A')) * power
            t_hash = t_hash * BASE + (ord(t[i]) - ord('A'))

        # final window check
        if t_hash == s_hash and t[-m:] == s:
            return len(t) - m
        
        return -1

