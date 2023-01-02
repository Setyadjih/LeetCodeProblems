from math import ceil


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        col_num = ceil(len(s) / ((2 * numRows) -2))
        outer = [[""] * col_num for _ in range(numRows)]
        curr_row = 0
        curr_col = 0
        l = 0
        while l < len(s):
            outer[curr_row][curr_col] = s[l]
            l += 1
            # fill vertical
            if curr_row != numRows - 1:
                curr_row += 1

            else:
                while curr_row != 0:
                    curr_row -= 1
                    curr_col += 1
                    outer[curr_row][curr_col] = s[l]
                    l += 1
                curr_row += 1

        # join rows ignoring blanks
        answer = ""
        for row in outer:
            answer += "".join(row)

        return answer





if __name__ == '__main__':
    print(Solution().convert("PAYPALISHIRING", 3))