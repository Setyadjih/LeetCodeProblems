import math


def max_sum(root) -> int:
    if not root:
        return float("-inf")
    if not root.left and not root.right:
        return root.val

    sum = root.value + max(max_sum(root.left), max_sum(root.right))
    return sum