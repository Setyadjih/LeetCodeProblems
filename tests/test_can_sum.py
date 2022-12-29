from problems.can_sum import can_sum


def test_can_sum():
    assert can_sum(7, [5, 3, 4, 7])


def test_can_sum2():
    assert not can_sum(7, [2, 4])


def test_can_sum3():
    assert not can_sum(300, [7, 14])

