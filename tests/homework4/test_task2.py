import pytest

from homework4.task2 import process_access_queries


@pytest.mark.parametrize(
    ("files", "queries", "expected"),
    [
        (
            {"a.txt": ["R", "W"]},
            [("read", "a.txt")],
            ["OK"]
        ),
        (
            {"a.txt": ["R", "W", "X"]},
            [("read", "a.txt"), ("write", "a.txt"), ("execute", "a.txt")],
            ["OK", "OK", "OK"]
        ),
        (
            {"a.txt": ["R"]},
            [("write", "a.txt")],
            ["Access denied"]
        ),
        (
            {"a.txt": ["R", "W"]},
            [("execute", "a.txt")],
            ["Access denied"]
        ),
        (
            {"a.txt": ["R"], "b.txt": ["R", "X"]},
            [("execute", "b.txt"), ("write", "a.txt"), ("read", "b.txt")],
            ["OK", "Access denied", "OK"],
        ),
    ],
)
def test_process_access_queries(files, queries, expected):
    assert process_access_queries(files, queries) == expected


def test_query_to_unknown_file_raises_key_error():
    with pytest.raises(KeyError):
        process_access_queries({"a.txt": ["R"]}, [("read", "b.txt")])


def test_source_data_is_not_modified():
    files = {"a.txt": ["R", "W"]}
    queries = [("write", "a.txt")]

    process_access_queries(files, queries)

    assert files == {"a.txt": ["R", "W"]}
    assert queries == [("write", "a.txt")]
