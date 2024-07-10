import pytest

from nrt_math_utils.math_utils import MathUtil
from nrt_math_utils.nrt_numbers import DecimalNumber
from tests.math_utils_data import average_data, max_data, min_data, floor_data, \
    sum_0_to_n_data


@pytest.mark.parametrize('numbers, weights, expected_average', average_data)
def test_average(numbers, weights, expected_average):
    average = MathUtil.average(numbers, weights)
    assert average == expected_average


def test_average_negative():
    with pytest.raises(ValueError):
        MathUtil.average([1, 2, 3], [1, 1])

    with pytest.raises(ValueError):
        MathUtil.average([1, 2], [1, 1, 1])

    with pytest.raises(ValueError):
        MathUtil.average([1, 2], [1, 'a'])

    with pytest.raises(ValueError):
        MathUtil.average([1, '2'], [1, 1])


@pytest.mark.parametrize('num, digits, expected_floor', floor_data)
def test_floor(num, digits, expected_floor):
    floor_num = MathUtil.floor(num, digits)
    assert floor_num == expected_floor


def test_is_all_numbers():
    assert MathUtil.is_all_numbers([1, 2])
    assert MathUtil.is_all_numbers([1, 2.0])
    assert MathUtil.is_all_numbers([1, 2.0, 0])
    assert MathUtil.is_all_numbers([0])
    assert MathUtil.is_all_numbers([DecimalNumber(0.0)])
    assert not MathUtil.is_all_numbers([DecimalNumber(0.0), 'a'])
    assert not MathUtil.is_all_numbers(['a', 1])
    assert not MathUtil.is_all_numbers(['a', 'b'])
    assert not MathUtil.is_all_numbers([True])
    assert not MathUtil.is_all_numbers([False])
    assert not MathUtil.is_all_numbers([None, 1])


@pytest.mark.parametrize('numbers, expected_max', max_data)
def test_max(numbers, expected_max):
    max_num = MathUtil.max(*numbers)
    assert max_num == expected_max


@pytest.mark.parametrize('numbers, expected_min', min_data)
def test_min(numbers, expected_min):
    min_num = MathUtil.min(*numbers)
    assert min_num == expected_min


@pytest.mark.parametrize('n, expected_sum', sum_0_to_n_data)
def test_sum_0_to_n(n, expected_sum):
    assert MathUtil.sum_0_to_n(n) == expected_sum
