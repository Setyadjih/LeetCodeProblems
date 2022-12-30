def all_construct(target, word_bank):
    table = [[] for _ in range(len(target) + 1)]
    table[0] = [[]]

    for i in range(len(target)):
        for word in word_bank:
            dest = i + len(word)

            if i + len(word) > len(target) + 1 or word != target[i:dest]:
                continue

            # copy all arrays from table[i] to destination
            new_combos = list(map(lambda x: [*x, word], table[i]))
            table[dest].extend(new_combos)

    return table[len(target)]


if __name__ == '__main__':
    arr = (all_construct("purple", ['purp', 'p', 'ur', 'le', 'purpl']))
    for ar in arr:
        print(ar)
