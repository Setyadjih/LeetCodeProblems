"""return an array containing the shortest combination of numbers that add up to the target"""
# e.g. best_sun(7, [5, 3, 4, 7]) -> [7]


def best_sum(target, numbers: list[int], memo=None):

    if memo is None:
        memo = {}

    if target in memo.keys():
        return memo[target].copy()

    if target == 0:
        return []

    if target < 0:
        return None

    shortest = None

    for n in numbers:
        remainder = target - n
        # This will only start to calculate once we hit the bottom and come back up
        # Although shortest will be assigned within the recursion calls, it gets scoped out when we come back up
        # So we'll only get the shortest for the top level call, where we get the full array
        result = best_sum(remainder, numbers, memo)
        # If we hit not None, that means the combination is good
        if result is not None:
            result.append(n)
            if shortest is None or len(result) < len(shortest):
                # we want to make sure we're passing by value here, since result may get changed in other recursions
                shortest = result.copy()

    if shortest:
        # We're also passing by value here
        memo[target] = shortest.copy()
    else:
        memo[target] = None

    # shortest may be none, so we may as well just return it normally
    return shortest


if __name__ == '__main__':
    r = best_sum(8, [1, 4, 5])
    print(r)