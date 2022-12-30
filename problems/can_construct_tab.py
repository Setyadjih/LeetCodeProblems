def can_construct(target, word_bank) -> bool:
    arr_len = len(target) + 1
    grid = [False] * (arr_len)
    grid[0] = True

    # We want to see if it's possible to hit the last one
    # iterate over every latter, not including the clear confirm
    for i in range(len(target)):
        if not grid[i]:
            continue
        for j in word_bank:
            # word must match to subtract
            if j != target[i:i+len(j)]:
                continue

            grid[i + len(j)] = True

    return grid[len(target)]


if __name__ == '__main__':
    res = can_construct("abcdef", ['ab', 'abc', 'cd', 'def', 'abcd'])
    print(res)