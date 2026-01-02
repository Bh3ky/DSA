"""
PROBLEM: You are given n versions and an API isBadVersion(version).
Find the first bad version.
"""

def firstBadVersion(n, isBadVersion):
    left, right = 1, n

    while left < right:
        mid = (left + right) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1

    return left