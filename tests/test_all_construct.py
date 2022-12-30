from all_construct import all_construct


def test_all_construct():
    assert all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']) == [
        ['purp', 'le'],
        ['p', 'ur', 'p', 'le']
    ]


def test_all_construct2():
    assert all_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']) == []


def test_all_constructs3():
    assert all_construct("aaaaaaaaaaaaaaaaaaaaz", ["a", "aa", "aaaa", "aaaaa"]) == []
