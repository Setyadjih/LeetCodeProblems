from collections import deque


def shortest_path(edge_list, start, end) -> int:
    # use a breadth first algorithm, using node distance pairs to find end
    graph = build_graph(edge_list)
    visited = set()
    distance = 0
    queue = deque()

    queue.append((start, distance))
    while queue:
        current, distance = queue.popleft()
        if current == end:
            return distance

        visited.add(current)

        for neighbor in graph[current]:
            if neighbor in visited:
                continue

            queue.append((neighbor, distance + 1))

    return -1


def build_graph(edge_list)-> dict:
    graph = {}
    for edge in edge_list:
        a, b = edge
        if a not in graph.keys():
            graph[a] = []
        if b not in graph.keys():
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph


if __name__ == '__main__':
    test = [
        ['a', 'b'],
        ['a', 'd'],
        ['b', 'c'],
        ['c', 'z'],
        ['d', 'z']
    ]

    print(shortest_path(test, 'a', 'z'))
    print(shortest_path(test, 'a', 'a'))
    print(shortest_path(test, 'a', 'g'))