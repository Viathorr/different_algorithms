import pytest
from ..array_sorting import QuickSort
from ..array_sorting_proxy import ArraySortingProxy


@pytest.fixture
def quick_sorting():
    quick_sorting = QuickSort()
    return ArraySortingProxy(quick_sorting)


def test_raises_type_error(quick_sorting, invalid_array):
    with pytest.raises(TypeError):
        quick_sorting.sort(invalid_array)


def test_sort_empty_array(quick_sorting, empty_array):
    quick_sorting.sort(empty_array)
    assert empty_array == []


def test_sort_one_element_array(quick_sorting, one_element_array):
    quick_sorting.sort(one_element_array)
    assert one_element_array == [1]


def test_sort_same_num_array(quick_sorting, same_num_array):
    quick_sorting.sort(same_num_array)
    assert same_num_array == [2, 2, 2, 2, 2, 2]


def test_sort_positive_array(quick_sorting, positive_array):
    quick_sorting.sort(positive_array)
    assert positive_array == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_sort_negative_array(quick_sorting, negative_array):
    quick_sorting.sort(negative_array)
    assert negative_array == [-9, -8, -7, -6, -5, -4, -3, -2, -1]


def test_sort_mixed_array(quick_sorting, mixed_array):
    quick_sorting.sort(mixed_array)
    assert mixed_array == [-34, -4, -1, 2, 3, 4, 9, 11]


def test_float_array(quick_sorting, float_nums_array):
    quick_sorting.sort(float_nums_array)
    assert float_nums_array == [-3.0, -2.7, -1.1, 0.5, 3.14, 5.6, 8.9]


def test_sort_string_array(quick_sorting, string_array):
    quick_sorting.sort(string_array)
    assert string_array == ['a', 'b', 'bewo', 'cwa', 'vda']
