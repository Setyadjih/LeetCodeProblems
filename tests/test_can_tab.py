from can_tab import can_tab


def test_can_tab():
    assert can_tab(7, [5, 4, 3])


def test_can_tab1():
    assert not can_tab(7, [2, 4])


def test_can_tab2():
    assert not can_tab(300, [7, 14])