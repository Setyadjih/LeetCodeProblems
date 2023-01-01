from collections import deque


def island_count(grid):
    count = 0
    done = set()
    
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 'W' or (row, col) in done:
                continue

            explore(grid, row, col, done)
            count += 1

    return count


def explore(grid, row, col, done):
    queue = deque()
    queue.append((row, col))

    # iterating depth first
    while queue:
        current = queue.pop()
        current_row, current_col = current

        if (current_row, current_col) in done or grid[current_row][current_col] == "W":
            continue
        done.add(current)

        # add neighbors
        if current_row > 0:
            queue.append((current_row-1, current_col))
        if current_row < len(grid) - 1:
            queue.append((current_row+1, current_col))
        if current_col > 0:
            queue.append((current_row, current_col-1))
        if current_col < len(grid[current_row]) -1:
            queue.append((current_row, current_col+1))


if __name__ == '__main__':
    grid = [
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'L', 'W', 'L', 'W'],
        ['W', 'W', 'L', 'L', 'W'],
        ['L', 'W', 'W', 'L', 'L'],
        ['L', 'L', 'W', 'W', 'W'],
    ]

    print(island_count(grid))
