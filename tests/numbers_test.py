import pytest

from nrt_math_utils.nrt_numbers import set_decimal_number_perc, DecimalNumber, \
    set_decimal_number_thousands_separator, unset_decimal_number_thousands_separator
from tests.numbers_data import \
    add_data, sub_data, multiple_data, truediv_data, pow_data, \
    equal_operator_data, equal_operator_negative_data, different_operator_data, \
    different_operator_negative_data, gt_operator_data, gt_operator_negative_data, \
    lt_operator_data, lt_operator_negative_data, ge_operator_data, \
    ge_operator_negative_data, le_operator_data, le_operator_negative_data, abs_data, \
    round_data, negative_data, int_data, radd_data, thousands_separator_data


@pytest.fixture(autouse=True)
def setup():
    perc = DecimalNumber(0).get_perc()
    set_decimal_number_perc(6)
    yield 'setup'
    set_decimal_number_perc(perc)


@pytest.mark.parametrize('num1, num2, expected_result', add_data)
def test_add(num1, num2, expected_result):
    result = num1 + num2
    assert result == expected_result, \
           f'Result is {result}, but it should be {expected_result}'


@pytest.mark.parametrize('num1, num2, expected_result', sub_data)
def test_sub(num1, num2, expected_result):
    result = num1 - num2
    assert result == expected_result, \
           f'Result is {result}, but it should be {expected_result}'


def test_str():
    num = DecimalNumber(1.12)
    assert str(num) == '1.12'


@pytest.mark.parametrize('num1, num2, expected_result', multiple_data)
def test_multiple(num1, num2, expected_result):
    result = num1 * num2
    assert result == expected_result, \
           f'Result is {result}, but it should be {expected_result}'


@pytest.mark.parametrize('num1, num2, expected_result', truediv_data)
def test_truediv(num1, num2, expected_result):
    result = num1 / num2
    assert result == expected_result, \
           f'Result is {result}, but it should be {expected_result}'


@pytest.mark.parametrize('num1, num2, expected_result', pow_data)
def test_pow(num1, num2, expected_result):
    result = num1 ** num2
    assert result == expected_result, \
           f'Result is {result}, but it should be {expected_result}'


@pytest.mark.parametrize('num1, num2', equal_operator_data)
def test_equal_operator(num1, num2):
    assert num1 == num2


@pytest.mark.parametrize('num1, num2', equal_operator_negative_data)
def test_equal_operator_negative(num1, num2):
    eq = num1 == num2
    assert not eq


@pytest.mark.parametrize('num1, num2', different_operator_data)
def test_different_operator(num1, num2):
    assert num1 != num2


@pytest.mark.parametrize('num1, num2', different_operator_negative_data)
def test_different_operator_negative(num1, num2):
    diff = num1 != num2
    assert not diff


@pytest.mark.parametrize('num1, num2', gt_operator_data)
def test_gt_operator(num1, num2):
    assert num1 > num2


@pytest.mark.parametrize('num1, num2', gt_operator_negative_data)
def test_gt_operator_negative(num1, num2):
    gt = num1 > num2
    assert not gt


@pytest.mark.parametrize('num1, num2', lt_operator_data)
def test_lt_operator(num1, num2):
    assert num1 < num2


@pytest.mark.parametrize('num1, num2', lt_operator_negative_data)
def test_lt_operator_negative(num1, num2):
    lt = num1 < num2
    assert not lt


@pytest.mark.parametrize('num1, num2', ge_operator_data)
def test_ge_operator(num1, num2):
    assert num1 >= num2


@pytest.mark.parametrize('num1, num2', ge_operator_negative_data)
def test_ge_operator_negative(num1, num2):
    ge = num1 >= num2
    assert not ge


@pytest.mark.parametrize('num1, num2', le_operator_data)
def test_le_operator(num1, num2):
    assert num1 <= num2


@pytest.mark.parametrize('num1, num2', le_operator_negative_data)
def test_le_operator_negative(num1, num2):
    le = num1 <= num2
    assert not le


@pytest.mark.parametrize('num, expected_result', abs_data)
def test_abs(num, expected_result):
    assert abs(num) == expected_result


def test_perc():
    num_1 = DecimalNumber(9.123456789, 8)
    assert num_1 == 9.12345679
    assert num_1.get_perc() == 8
    assert DecimalNumber.get_perc() == DecimalNumber.DEFAULT_PERC, \
           f'DecimalNumber.perc value is {DecimalNumber.get_perc()}' \
           f' but should be {DecimalNumber.DEFAULT_PERC}'
    DecimalNumber.set_perc(2)
    num_2 = DecimalNumber(4.1234)
    assert num_2 == 4.12
    DecimalNumber.set_perc(10)
    assert DecimalNumber.get_perc() == 10
    DecimalNumber.set_perc(DecimalNumber.DEFAULT_PERC)


@pytest.mark.parametrize('num, digits, expected_result', round_data)
def test_round(num, digits, expected_result):
    result = round(num, digits)
    assert result == expected_result, \
           f'Result of round {num} with {digits} digits is {result},' \
           f' but should be {expected_result}'


@pytest.mark.parametrize('num, expected_result', negative_data)
def test_negative(num, expected_result):
    assert -num == expected_result


@pytest.mark.parametrize('num, expected_result', int_data)
def test_int(num, expected_result):
    assert int(num) == expected_result


def test_dict_with_decimal_to_dict_with_float():
    dict_ = {
        'dec': DecimalNumber(11.1),
        'flt': 11.2,
        's': 'str',
        'dict': {
            'dict2': {
                'dec2': DecimalNumber(13.3)
            },
            'dec3': DecimalNumber(4),
            'none': None
        },
        'int': 11
    }

    expected_dict = {
        'dec': 11.1,
        'flt': 11.2,
        's': 'str',
        'dict': {
            'dict2': {
                'dec2': 13.3
            },
            'dec3': 4.0,
            'none': None
        },
        'int': 11
    }

    result_dict = \
        DecimalNumber.dict_with_decimal_to_dict_with_float(dict_)

    assert expected_dict == result_dict


@pytest.mark.parametrize('itr, expected_result', radd_data)
def test_radd_1(itr, expected_result: DecimalNumber):
    assert expected_result == sum(itr)


def test_radd_2():
    assert DecimalNumber(22) == 19 + DecimalNumber(3)
    assert DecimalNumber(22) == [10, 9] + DecimalNumber(3)


def test_rsub():
    assert DecimalNumber(16) == 19 - DecimalNumber(3)


def test_rmul():
    assert DecimalNumber(15) == 5 * DecimalNumber(3)
    assert DecimalNumber(18) == [2, 3] * DecimalNumber(3)


def test_rtruediv():
    assert DecimalNumber(6) == 18.0 / DecimalNumber(3)


def test_set_thousands_separator_update_separator_globally():
    assert str(DecimalNumber(1234567.89)) == '1234567.89'
    assert str(DecimalNumber(-1234567.89)) == '-1234567.89'

    set_decimal_number_thousands_separator()

    try:
        assert str(DecimalNumber(1234567.89)) == '1,234,567.89'
        assert str(DecimalNumber(-1234567.89)) == '-1,234,567.89'
        assert str(DecimalNumber(12)) == '12.0'
        assert str(DecimalNumber(-12)) == '-12.0'
        assert str(DecimalNumber(12000)) == '12,000.0'
        assert str(DecimalNumber(-12000)) == '-12,000.0'
        assert str(DecimalNumber(1.123)) == '1.123'
        assert str(DecimalNumber(-1.123)) == '-1.123'
    finally:
        unset_decimal_number_thousands_separator()
        assert str(DecimalNumber(1234)) == '1234.0'


@pytest.mark.parametrize('num, expected_str', thousands_separator_data)
def test_set_thousands_separator_update_separator_locally(num, expected_str):
    assert str(num) == expected_str


def test_set_thousands_separator_locally_false_globally_true():
    unset_decimal_number_thousands_separator()
    num = DecimalNumber(1234567.89, is_thousands_separator=True)
    assert str(num) == '1,234,567.89'
