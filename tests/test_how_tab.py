from how_tab import how_tab


def test_how_tab():
    assert how_tab(7, [5, 3, 4]) == [4, 3]


def test_how_tab1():
    assert how_tab(8, [2, 3, 5]) == [2, 2, 2, 2]


def test_how_tab2():
    assert how_tab(300, [7, 14]) is None
