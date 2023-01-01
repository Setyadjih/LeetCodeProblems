def find_max_component(graph):
    visited = set()
    glob_max = 0
    for n in graph.keys():
        component_size = explore(graph, n, visited)
        glob_max = max(glob_max, component_size)

    return glob_max


def explore(graph, current, visited) -> int:
    count = 0
    if current in visited:
        return count
    visited.add(current)
    count += 1

    for n in graph[current]:
        count += explore(graph, n, visited)

    print(visited)
    return count


if __name__ == '__main__':
    test = {
        0: [1],
        1: [0, 2],
        2: [1],
        3: []
    }

    print(find_max_component(test))