"""given a target sum and array, return an array that sums up to the target"""


def how_sum(target, numbers, memo=None):
    if memo is None:
        memo = {}

    if target == 0:
        return []

    if target in memo.keys():
        return memo[target]

    if target < 0:
        memo[target] = None
        return None

    for n in numbers:
        remainder = target - n
        result = how_sum(remainder, numbers, memo)
        if result is not None:
            result.append(n)
            memo[target] = result
            return result

    memo[target] = None
    return None


if __name__ == '__main__':
    print(how_sum(7, [2, 3]))
