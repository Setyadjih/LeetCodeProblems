from collections import deque


def bst_depth(root):
    if not root:
        return []
    values = []
    stack = deque(root)

    while stack:
        current = stack.popleft()
        values.append(current.value)

        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

    return values


if __name__ == '__main__':
    print(bst_depth(None))