import pytest

from homework2.optional_version.DSU import DSU


def test_new_elements_are_separate_sets():
    dsu = DSU(5)

    assert [dsu.find(i) for i in range(5)] == [0, 1, 2, 3, 4]


def test_find_of_root_without_union_returns_itself():
    dsu = DSU(3)

    assert dsu.find(2) == 2


def test_union_merges_two_sets():
    dsu = DSU(5)
    dsu.union(1, 2)

    assert dsu.find(1) == dsu.find(2)
    assert dsu.find(1) != dsu.find(3)


def test_union_returns_true_for_different_sets():
    dsu = DSU(5)

    assert dsu.union(0, 1)
    assert dsu.union(2, 3)


def test_union_returns_false_for_same_set():
    dsu = DSU(5)
    dsu.union(1, 2)
    dsu.union(2, 3)

    assert not dsu.union(1, 3)
    assert not dsu.union(2, 2)


def test_chain_of_unions_forms_one_set():
    dsu = DSU(6)
    for i in range(5):
        dsu.union(i, i + 1)

    assert len(set(dsu.find(i) for i in range(6))) == 1


def test_repeated_union_does_not_change_number_of_sets():
    dsu = DSU(4)
    dsu.union(0, 1)
    roots_before = set(dsu.find(i) for i in range(4))

    for _ in range(3):
        dsu.union(0, 1)

    assert set(dsu.find(i) for i in range(4)) == roots_before