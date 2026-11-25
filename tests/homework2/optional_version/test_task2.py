import pytest

from homework2.optional_version.task2 import find_components


@pytest.mark.parametrize(
    ("vertices_number", "edges", "expected"),
    [
        (4, [(1, 2), (3, 4)], [1, 1, 2, 2]),
        (5, [(1, 2), (2, 3), (3, 4), (4, 5)], [1, 1, 1, 1, 1]),
        (5, [], [1, 2, 3, 4, 5]),
        (6, [(1, 2), (2, 3)], [1, 1, 1, 2, 3, 4]),
        (5, [(1, 2), (1, 3), (1, 4), (1, 5)], [1, 1, 1, 1, 1]),
        (1, [], [1]),
    ],
)
def test_find_components(vertices_number, edges, expected):
    assert find_components(vertices_number, edges) == expected


@pytest.mark.parametrize(
    ("vertices_number", "edges"),
    [
        (4, [(1, 2), (3, 4)]),
        (10, [(1, 2), (2, 3), (7, 8)]),
        (10, [(i, i + 1) for i in range(1, 10)]),
        (6, []),
    ],
)
def test_components_are_numbered_from_one_to_l(vertices_number, edges):
    components = find_components(vertices_number, edges)

    assert len(components) == vertices_number
    assert sorted(set(components)) == list(range(1, len(set(components)) + 1))


def test_result_does_not_depend_on_edge_order():
    edges = [(1, 2), (3, 4), (2, 3)]

    assert find_components(4, edges) == find_components(4, list(reversed(edges)))