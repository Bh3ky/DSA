import pytest
from solution_2 import firstBadVersion

def test_first_bad_version_middle():
    bad = 4

    def isBadVersion(version):
        return version >= bad

    assert firstBadVersion(10, isBadVersion) == 4

def test_first_bad_version_first():
    bad = 1

    def isBadVersion(version):
        return version >= bad

    assert firstBadVersion(5, isBadVersion) == 1

def test_first_bad_version_last():
    bad = 7

    def isBadVersion(version):
        return version >= bad

    assert firstBadVersion(7, isBadVersion) == 7