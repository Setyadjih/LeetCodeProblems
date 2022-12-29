"""can the target sum be found in the array of numbers"""


def can_sum(target_sum: int, numbers: list[int], memo=None) -> bool:
    # handle base cases first
    if memo is None:
        memo = {}
    if target_sum == 0:
        return True
    if target_sum in memo.keys():
        return memo[target_sum]

    for n in numbers:
        if n > target_sum:
            continue
        remainder = target_sum - n
        if can_sum(remainder, numbers, memo):
            return True

    memo[target_sum] = False
    return False
