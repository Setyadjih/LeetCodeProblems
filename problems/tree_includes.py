def tree_includes(root, target) -> bool:
    if not root:
        return False
    if root == target:
        return True

    left = tree_includes(root.left, target)
    right = tree_includes(root.right, target)

    if left or right:
        return True
    return False
