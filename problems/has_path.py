from collections import deque

graph = {
    "f": ['g', 'i'],
    "g": ['h'],
    "h": [],
    "i": ['g', 'k'],
    "j": ['i'],
    "k": []
}


def has_path(graph, start, end):
    stack = deque()
    stack.append(start)
    while stack:
        current = stack.popleft()
        if current == end:
            return True
        for n in graph[current]:
            stack.appendleft(n)

    return False


if __name__ == '__main__':
    print(has_path(graph, 'f', 'k'))  # True
