from can_construct import can_construct


def test_can_construct():
    assert can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
        "e",
        "ee",
        "eee",
        "eeeee",
        "eeeeeeeeeeeeeeee",
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
        "f"
    ])
