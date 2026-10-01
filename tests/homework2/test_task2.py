import pytest

from homework2.task2 import calculate_perimeter


@pytest.mark.parametrize(
    ("figure", "expected"),
    [
        ([(1, 1)], 4),
        ([(8, 8)], 4),
        ([(4, 5)], 4),
        ([(1, 1), (1, 2)], 6),
        ([(1, 1), (2, 1)], 6),
        ([(1, 1), (1, 2), (2, 1)], 8),
    ],
)
def test_small_figures(figure, expected):
    assert calculate_perimeter(figure) == expected


@pytest.mark.parametrize("size", [1, 2, 3, 4, 5, 6, 7, 8])
def test_full_square(size):
    figure = [(r, c) for r in range(1, size + 1) for c in range(1, size + 1)]
    assert calculate_perimeter(figure) == 4 * size


@pytest.mark.parametrize(
    "length",
    [1, 2, 3, 4, 5, 6, 7, 8],
)
@pytest.mark.parametrize("horizontal", [True, False])
def test_strip(length, horizontal):
    if horizontal:
        figure = [(4, c) for c in range(1, length + 1)]
    else:
        figure = [(r, 4) for r in range(1, length + 1)]
    assert calculate_perimeter(figure) == 2 * (length + 1)


def test_u_shape_figure():
    figure = [(1, 1), (1, 2), (2, 2), (3, 1), (3, 2)]
    assert calculate_perimeter(figure) == 12


def test_plus_shape():
    figure = [(2, 3), (3, 2), (3, 3), (3, 4), (4, 3)]
    assert calculate_perimeter(figure) == 12


def test_o_shape_figure():
    figure = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2), (4, 1), (4, 2), (4, 2)]
    assert calculate_perimeter(figure) == 20


def test_full_board_minus_interior_cell_adds_four():
    figure = [(r, c) for r in range(1, 9) for c in range(1, 9)]
    assert calculate_perimeter(figure) == 32
    figure.remove((4, 4))
    assert calculate_perimeter(figure) == 36


def test_full_board_minus_side_cell_adds_two():
    figure = [(r, c) for r in range(1, 9) for c in range(1, 9)]
    assert calculate_perimeter(figure) == 32
    figure.remove((2, 1))
    assert calculate_perimeter(figure) == 34


def test_full_board_minus_corner_keeps_perimeter():
    figure = [(r, c) for r in range(1, 9) for c in range(1, 9)]
    figure.remove((1, 1))
    assert calculate_perimeter(figure) == 32


def test_is_independent_of_cell_order():
    figure = [(1, 1), (1, 2), (2, 1), (2, 2), (3, 3)]
    assert calculate_perimeter(figure) == calculate_perimeter(list(reversed(figure)))