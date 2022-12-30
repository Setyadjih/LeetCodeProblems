

def count_construct(target, wordbank) -> int:
    table = [0] * (len(target) + 1)

    # Handle "" case
    table[0] = 1

    for i in range(len(target)):
        if table[i] == 0:
            continue

        for word in wordbank:
            if word != target[i:i+len(word)]:
                continue

            # each index represents how many ways there are to get to that point, so it carries over
            table[i + len(word)] += table[i]

    print(table)
    return table[len(target)]


if __name__ == '__main__':
    print(count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
