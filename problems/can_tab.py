def can_tab(target, nums) -> bool:
    grid = [False] * (target + 1)
    grid[0] = True

    # target + 1 is the end of the grid, due to off-by-one errors
    for i in range(target + 1):
        if not grid[i]:
            continue

        for j in range(len(nums)):
            if i + nums[j] <= target:
                grid[i+nums[j]] = True

    return grid[target]


if __name__ == '__main__':
    print(can_tab(7, [5, 4, 3]))