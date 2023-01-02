"""determine the size of the smallest island"""


def min_island(grid):
    min_size = None
    done = set()

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            island_size = explore(grid, r, c, done)
            if island_size == 0:
                continue
            min_size = min(min_size, island_size) if min_size else island_size

    return min_size


def explore(grid, r, c, done):
    # Check for validity
    valid_r = 0 <= r < len(grid)
    if not valid_r:
        return 0
    valid_c = 0 <= c < len(grid[r])
    if not valid_c:
        return 0

    if grid[r][c] == 'W':
        return 0

    if (r, c) in done:
        return 0

    done.add((r, c))

    # explore neighbors
    size = 1
    size += explore(grid, r+1, c, done)
    size += explore(grid, r-1, c, done)
    size += explore(grid, r, c+1, done)
    size += explore(grid, r, c-1, done)

    return size




if __name__ == '__main__':
    grid = [
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'L', 'W'],
        ['W', 'W', 'L', 'L', 'W'],
        ['L', 'W', 'W', 'L', 'L'],
        ['L', 'L', 'W', 'W', 'W'],
    ]

    print(min_island(grid))
