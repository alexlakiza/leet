"""
Given two binary strings a and b, return their sum as a binary string.
"""


class Solution:
    def add_binary(self, a: str, b: str) -> str:
        return (bin(int(a, 2) + int(b, 2)))[2:]


if __name__ == "__main__":
    s = Solution()
    assert s.add_binary(a = "11", b = "1") == "100"
