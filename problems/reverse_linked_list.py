def reverse_list(head):
    prev = None
    current = head

    while current is not None:
        next = current.next

        # reverse link
        current.next = prev

        # Shift pointers
        prev = current
        current = next

    return prev


def reverse_list_recursive(head):
    prev = None
    current = head
    last = helper(current, prev)
    return last


def helper(current, prev):
    if current is None:
        return prev

    next = current.next
    current.next = prev
    return helper(next, current)