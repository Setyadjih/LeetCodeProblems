"""given a word and a list of strings, can the word be constructed?"""


def can_construct(word, substrings, memo=None) -> bool:
    if memo is None:
        memo = {}
    if word == '':
        return True  # return an empty array
    if word in memo.keys():
        return memo[word]

    for s in substrings:
        # Only subtract if the front matches
        if s == word[:len(s)]:
            # slice off the substring
            remainder = word.replace(s, '')
            result = can_construct(remainder, substrings)
            if result:
                memo[word] = result
                return True

    memo[word] = False
    return False


if __name__ == '__main__':
    print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
