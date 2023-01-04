def tree_sum(root):
    if not root:
        return 0
    total = child_sum(root)
    return total


def child_sum(root) -> int:
    if not root:
        return 0
    total = root.val
    total += child_sum(root.left)
    total += child_sum(root.right)
    return total

# ------------
class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


a = Node(1)
b = Node(6)
c = Node(0)
d = Node(3)
e = Node(-6)
f = Node(2)
g = Node(2)
h = Node(2)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#      1
#    /   \
#   6     0
#  / \     \
# 3   -6    2
#    /       \
#   2         2
if __name__ == '__main__':

    assert tree_sum(a) == 10  # -> 10
