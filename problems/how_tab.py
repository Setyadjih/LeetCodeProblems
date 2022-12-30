"""return at least 1 way to create the target. Return null if not possible"""


def how_tab(target, nums):
    grid = [None] * (target+1)
    grid[0] = []

    for i in range(target+1):
        if grid[i] is None:
            continue

        for j in nums:
            if i + j > target:
                continue
            combined: list = grid[i].copy()
            combined.append(j)
            grid[i + j] = combined.copy()

    print(f"{grid} -{target}-> {grid[target]}")
    return grid[target]


if __name__ == '__main__':
    res = how_tab(7, [5, 3, 4])
    print(res)