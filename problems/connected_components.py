"""Given an undirected graph, the task is to print all the connected components line by line. """
from collections import deque


def connected_components(graph: dict) -> int:
    count = 0
    done = set()
    for node in graph.keys():
        if explore(graph, node, done):
            count += 1

    return count


def explore(graph, current, done):
    if current in done:
        return False
    done.add(current)
    for neighbor in graph[current]:
        explore(graph, neighbor, done)

    return True


if __name__ == '__main__':
    test = {
        0: [8, 1, 5],
        1: [0],
        5: [0, 8],
        8: [0, 5],
        2: [3, 4],
        3: [2, 4],
        4: [3, 2]
    }

    print(connected_components(test))
