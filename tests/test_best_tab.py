from best_tab import best_tab


def test_best_tab():
    assert best_tab(7, [5, 3, 4, 7]) == [7]


def test_best_tab1():
    assert best_tab(8, [1, 4, 5]) == [4, 4]


def test_best_tab2():
    assert best_tab(100, [1, 2, 5, 25]) == [25, 25, 25, 25]