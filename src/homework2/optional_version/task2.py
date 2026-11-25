from homework2.optional_version.DSU import DSU


def find_components(vertices_number: int, edges: list[tuple[int, int]]) -> list[int]:
    """Находит компоненты связности и возвращает список с номерами компоненты связности для вершины, начиная 1."""
    dsu = DSU(vertices_number + 1)

    for u, v in edges:
        dsu.union(u, v)

    component_numbers: dict[int, int] = {}
    components = []

    for vertex in range(1, vertices_number + 1):
        root = dsu.find(vertex)
        if root not in component_numbers:
            component_numbers[root] = len(component_numbers) + 1
        components.append(component_numbers[root])

    return components


if __name__ == "__main__":
    n, m = map(int,input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]

    components = find_components(n, edges)

    print(len(set(components)))
    print(*components)