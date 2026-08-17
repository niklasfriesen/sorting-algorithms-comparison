from algorithms.bubble_sort import bubble_sort


def test_empty_list():
    assert bubble_sort([]) == []

def test_single_element():
    assert bubble_sort([5]) == [5]

def test_already_sorted():
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_reverse_sorted():
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_duplicates():
    assert bubble_sort([3, 1, 2, 3, 1]) == [1, 1, 2, 3, 3]

def test_negative_numbers():
    assert bubble_sort([-3, 5, -1, 0, -5]) == [-5, -3, -1, 0, 5]

def test_does_not_change_input():
    original = [3, 1, 2]
    bubble_sort(original)
    assert original == [3, 1, 2]