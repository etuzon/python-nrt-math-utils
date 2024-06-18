from nrt_math_utils.nrt_numbers import DecimalNumber

average_data = [
    ([1, 2, 3], [1, 1, 1], DecimalNumber(2)),
    ([1, 2, 3], [1, 2, 3], DecimalNumber(2.333333)),
    ([1, 2, 3], [3, 2, 1], DecimalNumber(1.666667)),
    ([1, 2, 3], [1, 1, 1], DecimalNumber(2)),
    ([1, 2, 3], None, DecimalNumber(2)),
    ([1], [1], DecimalNumber(1)),
    ([1, 2], [1, 1], DecimalNumber(1.5)),
    ([1, 2], [1, 2], DecimalNumber(1.666667)),
    ([1, 2], [2, 1], DecimalNumber(1.333333)),
    ([1, 2], [2, 2], DecimalNumber(1.5))
]

floor_data = [
    (1.2345, 2, 1.23),
    (1.2345, 3, 1.234),
    (1.2345, 4, 1.2345),
    (1.2345, 5, 1.2345)
]

max_data = [
    ([1, 2, 3], 3),
    ([1, 2, 3, 3], 3),
    ((1, 7, 6), 7),
    ([1, [2, 3], 4], 4),
    ([5, [66, 7], 8], 66),
    ([-1, -2, -3], -1),
    ((0, 0), 0),
    ([None, 1, 2], 2),
    ([None, None, None], None),
    ([None], None),
    ([], None),
    ([None, None, 1], 1)
]

min_data = [
    ([1, 2, 3], 1),
    ([1, 2, 3, 3], 1),
    ((1, 7, 6), 1),
    ([1, [2, 3], 4], 1),
    ([5, [66, 7], 8], 5),
    ([-1, -2, -3], -3),
    ((0, 0), 0),
    ([None, 1, 2], 1),
    ([None, None, None], None),
    ([None], None),
    ([], None),
    ([None, None, 1], 1)
]
