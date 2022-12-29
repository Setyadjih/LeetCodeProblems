from best_sum import best_sum


def test_best_sum():
    assert best_sum(7, [5, 3, 4, 7]) == [7]


def test_best_sum2():
    assert best_sum(8, [1, 4, 5]) == [4, 4]


def test_best_sum3():
    assert best_sum(100, [1, 2, 5, 25]) == [25, 25, 25, 25]