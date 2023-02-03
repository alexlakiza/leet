"""
Given an integer x, return true if x is a palindrome, and false otherwise.
"""


class Solution:
    def is_palindrome(self, x: int) -> bool:
        if str(x) != str(x)[::-1]:
            return False
        else:
            return True
