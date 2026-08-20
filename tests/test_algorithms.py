import pytest

from src.algorithms.bubble_sort import bubble_sort
from src.algorithms.heap_sort import heap_sort
from src.algorithms.insertion_sort import insertion_sort
from src.algorithms.merge_sort import merge_sort
from src.algorithms.quick_sort import quick_sort
from src.algorithms.selection_sort import selection_sort

SORT_FUNCTIONS = [
    bubble_sort,
    heap_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    selection_sort,
]


@pytest.mark.parametrize("sort_func", SORT_FUNCTIONS)
def test_empty_list(sort_func):
    assert sort_func([]) == []


@pytest.mark.parametrize("sort_func", SORT_FUNCTIONS)
def test_single_element(sort_func):
    assert sort_func([5]) == [5]


@pytest.mark.parametrize("sort_func", SORT_FUNCTIONS)
def test_already_sorted(sort_func):
    assert sort_func([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


@pytest.mark.parametrize("sort_func", SORT_FUNCTIONS)
def test_reverse_sorted(sort_func):
    assert sort_func([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


@pytest.mark.parametrize("sort_func", SORT_FUNCTIONS)
def test_duplicates(sort_func):
    assert sort_func([3, 1, 2, 3, 1]) == [1, 1, 2, 3, 3]


@pytest.mark.parametrize("sort_func", SORT_FUNCTIONS)
def test_negative_numbers(sort_func):
    assert sort_func([-3, 5, -1, 0, -5]) == [-5, -3, -1, 0, 5]


@pytest.mark.parametrize("sort_func", SORT_FUNCTIONS)
def test_does_not_change_input(sort_func):
    original = [3, 1, 2]
    sort_func(original)
    assert original == [3, 1, 2]