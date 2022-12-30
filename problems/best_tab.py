def best_tab(target: int, nums: list[int]) -> list[int]:
    table = [None] * (target + 1)
    table[0] = []

    for i in range(target + 1):
        # unreachable sum
        if table[i] is None:
            continue

        for j in nums:
            if i + j > target:
                continue

            combined = [*table[i], j]
            if table[i + j] is None or len(table[i + j]) >= len(combined):
                table[i + j] = combined

    return table[target]


if __name__ == '__main__':
    res = best_tab(7, [5, 3, 4, 7])
    print(res)
