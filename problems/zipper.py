def zipper_list(head1, head2):
    c1 = head1.next
    c2 = head2
    count = 0
    # init new list
    tail = c1

    while c1 is not None or c2 is not None:
        # toggle by even or odd
        even = True if count % 2 == 0 else False

        # append by even or odd
        if even:
            tail.next = c2
            c2 = c2.next
        else:
            tail.next = c1
            c1 = c1.next

        tail = tail.next
        count += 1

    # one remains unfinished, append remaining
    if c1 or c2:
        tail.next = c1 if c1 is not None else c2

    return tail.next

