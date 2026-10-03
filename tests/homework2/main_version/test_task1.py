import pytest

from homework2.main_version.task1 import count_placement_positions


@pytest.mark.parametrize(
    ("field", "expected"),
    [
        (["."], 1),
        (["*"], 0),
        ([".."], 2),
        (["**"], 0),
        (["*."], 0),
        ([".*"], 0),
        (["*..."], 2),
        (["..*."], 1),
        (["*.*."], 0),
        ([".*.*"], 0),
        (["...."], 4),
    ],
)
def test_single_row(field, expected):
    assert count_placement_positions(field) == expected


@pytest.mark.parametrize(
    ("field", "expected"),
    [
        (
            [
                "****",
                "**..",
                "*...",
                "*...",
            ],
            4,
        ),
        (
            [
                "***",
                "...",
                "...",
                "***",
            ],
            0,
        ),
        (
            [
                "*.*.",
                ".*.*",
                "*.*.",
                ".*.*",
                "*.*.",
            ],
            0,
        ),
    ],
)
def test_more_than_one_row_field(field, expected):
    assert count_placement_positions(field) == expected


def test_single_available_column():
    assert count_placement_positions(["*", ".", "."]) == 1


def test_star_blocks_its_neighbour_in_single_column():
    assert count_placement_positions(["*", "*", "."]) == 0


@pytest.mark.parametrize("n", [1, 5, 10])
@pytest.mark.parametrize("m", [1, 5, 10])
def test_empty_field_has_all_cells_available(n, m):
    assert count_placement_positions(["." * m for _ in range(n)]) == n * m


@pytest.mark.parametrize("n", [1, 7])
@pytest.mark.parametrize("m", [1, 7])
def test_full_field_has_no_available_cells(n, m):
    assert count_placement_positions(["*" * m for _ in range(n)]) == 0


def test_symmetric_field_should_return_same_result():
    field = [
        "*..*",
        "....",
        "..*.",
        "*..*",
    ]
    assert count_placement_positions(field) == count_placement_positions(
        [row[::-1] for row in field]
    )
