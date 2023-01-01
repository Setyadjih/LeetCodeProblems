from collections import deque

graph = {
    "a": ['b', 'c'],
    "b": ['d'],
    "c": ["e"],
    "d": ['f'],
    "e": [],
    "f": []
}


def depth_first_print(graph, start):
    stack = deque()
    stack.appendleft(start)
    while stack:
        current = stack.popleft()
        print(current, end='')
        for neighbor in graph[current]:
            stack.appendleft(neighbor)


# Using the call stack as your stack
def depth_recursive(graph, start):
    print(start, end="")
    for neighbor in graph[start]:
        depth_recursive(graph, neighbor)


def breadth_first_print(graph, start):
    stack = deque()
    stack.appendleft(start)
    while stack:
        current = stack.pop()
        print(current, end='')
        for n in graph[current]:
            stack.appendleft(n)


if __name__ == '__main__':
    print("depth: ", end="")
    depth_first_print(graph, "a")
    print()
    print("depth recursive: ", end="")
    depth_recursive(graph, "a")
    print()
    print("breadth: ", end="")
    breadth_first_print(graph, "a")

