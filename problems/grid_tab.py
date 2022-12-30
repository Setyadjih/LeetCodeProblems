"Grid traveler with tabulation"


def grid_tab(m, n):
    table = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    table[1][1] = 1

    for row in range(n + 1):
        for col in range(m + 1):
            # add value to left and right
            current = table[row][col]
            if col + 1 <= n:
                table[row][col + 1] += current

            if row + 1 <= m:
                table[row + 1][col] += current

    for l in table:
        print(l)
    print()

    return table[n][m]


if __name__ == '__main__':
    print(grid_tab(2, 2))