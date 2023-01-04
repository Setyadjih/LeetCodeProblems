import sys


def min_tree(root) -> int:
    if not root:
        return sys.maxsize

    result = [root.val]
    left = min_tree(root.left) if root.left else None
    right = min_tree(root.right) if root.right else None

    if left:
        result.append(left)
    if right:
        result.append(right)

    return min(result)

