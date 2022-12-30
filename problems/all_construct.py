def all_construct(target: str, word_bank: list[str], memo=None) -> list[list[str]]:
    # handle base cases
    if memo is None:
        memo = {}
    if target == "":
        return [[]]
    if target in memo.keys():
        return memo[target]

    result = []
    # recurse through word_bank to breakdown word
    for w in word_bank:
        if not target.startswith(w):
            continue

        suffix = target[len(w):]
        suffix_ways = all_construct(suffix, word_bank)
        for way in suffix_ways:
            way.insert(0, w)
            result.extend(suffix_ways)
        memo[target] = result

    memo[target] = result
    return result


if __name__ == '__main__':
    print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
