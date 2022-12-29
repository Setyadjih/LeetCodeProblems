from how_sum import how_sum


def test_how_sum():
    assert how_sum(7, [2, 3]) == [3, 2, 2]


def test_how_sum1():
    assert how_sum(7, [5, 3, 4, 7]) == [4, 3]


def test_how_sum2():
    assert not how_sum(300, [7, 14])