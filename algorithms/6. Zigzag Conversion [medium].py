"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        else:
            ind = 0
            kek = [[] for i in range(numRows)]
            for i, val in enumerate(s):
                kek[ind].append(val)

                if (i // (numRows - 1)) % 2 == 0:
                    ind += 1
                else:
                    ind -= 1
            return ''.join([''.join(_) for _ in kek])
