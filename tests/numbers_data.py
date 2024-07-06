from nrt_math_utils.nrt_numbers import DecimalNumber

add_data = [
    (DecimalNumber(1), DecimalNumber(3), DecimalNumber(4)),
    (DecimalNumber(-1), DecimalNumber(3), DecimalNumber(2)),
    (DecimalNumber(5.5), DecimalNumber(7.1), DecimalNumber(12.6)),
    (DecimalNumber(0), DecimalNumber(3.2), DecimalNumber(3.2)),
    (DecimalNumber(1.1), 3, DecimalNumber(4.1)),
    (DecimalNumber(1.2), 3.2, DecimalNumber(4.4))
]

sub_data = [
    (DecimalNumber(1), DecimalNumber(3), DecimalNumber(-2)),
    (DecimalNumber(-1), DecimalNumber(3), DecimalNumber(-4)),
    (DecimalNumber(5.5), DecimalNumber(7.1), DecimalNumber(-1.6)),
    (DecimalNumber(0), DecimalNumber(3.2), DecimalNumber(-3.2)),
    (DecimalNumber(1.1), 3, DecimalNumber(-1.9)),
    (DecimalNumber(1.2), 3.2, DecimalNumber(-2))
]

multiple_data = [
    (DecimalNumber(1), DecimalNumber(3), DecimalNumber(3)),
    (DecimalNumber(-1), DecimalNumber(-3), DecimalNumber(3)),
    (DecimalNumber(5.5), DecimalNumber(7.1), DecimalNumber(39.05)),
    (DecimalNumber(0), DecimalNumber(3.2), DecimalNumber(0)),
    (DecimalNumber(1.1), 3, DecimalNumber(3.3)),
    (DecimalNumber(1.2), 3.2, DecimalNumber(3.84))
]

truediv_data = [
    (DecimalNumber(1), DecimalNumber(1), DecimalNumber(1)),
    (DecimalNumber(-1), DecimalNumber(-4), DecimalNumber(0.25)),
    (DecimalNumber(10), DecimalNumber(4), DecimalNumber(2.5)),
    (DecimalNumber(0), DecimalNumber(3.2), DecimalNumber(0)),
    (DecimalNumber(9), 3, DecimalNumber(3)),
    (DecimalNumber(-9), 6, DecimalNumber(-1.5))
]

pow_data = [
    (DecimalNumber(1), DecimalNumber(1), DecimalNumber(1)),
    (DecimalNumber(-2), DecimalNumber(2), DecimalNumber(4)),
    (DecimalNumber(10), DecimalNumber(3), DecimalNumber(1000)),
    (DecimalNumber(0), DecimalNumber(3.2), DecimalNumber(0)),
    (DecimalNumber(9), 2.5, DecimalNumber(243)),
    (DecimalNumber(-9), 6, DecimalNumber(531441))
]

equal_operator_data = [
    (DecimalNumber(1), DecimalNumber(1)),
    (DecimalNumber(2), DecimalNumber(2)),
    (DecimalNumber(0), DecimalNumber(0)),
    (DecimalNumber(0), 0),
    (DecimalNumber(9), 9),
    (DecimalNumber(-9.555), -9.555),
    (5, DecimalNumber(5)),
    (0, DecimalNumber(0))
]

equal_operator_negative_data = [
    (DecimalNumber(1), DecimalNumber(1.1)),
    (DecimalNumber(2), DecimalNumber(-2)),
    (DecimalNumber(0), DecimalNumber(0.1)),
    (DecimalNumber(0), -0.01),
    (DecimalNumber(9), 19),
    (DecimalNumber(-9.555), 9.555)
]

different_operator_data = [
    (DecimalNumber(1), DecimalNumber(1.1)),
    (DecimalNumber(2), DecimalNumber(-2)),
    (DecimalNumber(0), DecimalNumber(0.1)),
    (DecimalNumber(0), -0.01),
    (DecimalNumber(9), 19),
    (DecimalNumber(-9.555), 9.555),
    (5, DecimalNumber(5.1)),
    (0, DecimalNumber(0.1))
]

different_operator_negative_data = [
    (DecimalNumber(1), DecimalNumber(1)),
    (DecimalNumber(2), DecimalNumber(2)),
    (DecimalNumber(0), DecimalNumber(0)),
    (DecimalNumber(0), 0),
    (DecimalNumber(9), 9),
    (DecimalNumber(-9.555), -9.555)
]

gt_operator_data = [
    (DecimalNumber(1), DecimalNumber(0.99)),
    (DecimalNumber(2), DecimalNumber(-2)),
    (DecimalNumber(0), DecimalNumber(-0.1)),
    (DecimalNumber(0), -90),
    (DecimalNumber(9), 8),
    (DecimalNumber(-9.555), -19.555)
]

gt_operator_negative_data = [
    (DecimalNumber(-11), DecimalNumber(-1.1)),
    (DecimalNumber(2), DecimalNumber(2)),
    (DecimalNumber(0), DecimalNumber(0.1)),
    (DecimalNumber(0), 0.01),
    (DecimalNumber(9), 9),
    (DecimalNumber(-9.555), 9.555)
]

lt_operator_data = [
    (DecimalNumber(1), DecimalNumber(1.99)),
    (DecimalNumber(2), DecimalNumber(22)),
    (DecimalNumber(0), DecimalNumber(0.1)),
    (DecimalNumber(-10.102), 90),
    (DecimalNumber(9), 18),
    (DecimalNumber(-9.555), 19.555)
]

lt_operator_negative_data = [
    (DecimalNumber(1), DecimalNumber(-1.1)),
    (DecimalNumber(2), DecimalNumber(2)),
    (DecimalNumber(1), DecimalNumber(0.1)),
    (DecimalNumber(20), 0.01),
    (DecimalNumber(9), 9),
    (DecimalNumber(19.555), 9.555)
]

ge_operator_data = [
    (DecimalNumber(1), DecimalNumber(0.99)),
    (DecimalNumber(2), DecimalNumber(2)),
    (DecimalNumber(0), DecimalNumber(-0.1)),
    (DecimalNumber(0), -90),
    (DecimalNumber(9), 9),
    (DecimalNumber(-9.555), -19.555)
]

ge_operator_negative_data = [
    (DecimalNumber(-11), DecimalNumber(-1.1)),
    (DecimalNumber(2), DecimalNumber(2.1)),
    (DecimalNumber(0), DecimalNumber(0.1)),
    (DecimalNumber(0), 0.01),
    (DecimalNumber(9), 9.001),
    (DecimalNumber(-9.555), 9.555)
]

le_operator_data = [
    (DecimalNumber(1), DecimalNumber(1.99)),
    (DecimalNumber(22), DecimalNumber(22)),
    (DecimalNumber(0), DecimalNumber(0.1)),
    (DecimalNumber(-10.102), 90),
    (DecimalNumber(9), 18),
    (DecimalNumber(-9.555), -9.555)
]

le_operator_negative_data = [
    (DecimalNumber(1), DecimalNumber(-1.1)),
    (DecimalNumber(2), DecimalNumber(-2)),
    (DecimalNumber(1), DecimalNumber(0.1)),
    (DecimalNumber(20), 0.01),
    (DecimalNumber(9), 8),
    (DecimalNumber(19.555), 1.555)
]

abs_data = [
    (DecimalNumber(1), DecimalNumber(1)),
    (DecimalNumber(2), DecimalNumber(2)),
    (DecimalNumber(-1.1), DecimalNumber(1.1)),
    (DecimalNumber(20), DecimalNumber(20)),
    (DecimalNumber(-9), DecimalNumber(9)),
    (DecimalNumber(19.555), DecimalNumber(19.555))
]

round_data = [
    (DecimalNumber(11.1111), 2, DecimalNumber(11.11)),
    (DecimalNumber(22.33331111), None, 22)
]

negative_data = [
    (DecimalNumber(11.1111), DecimalNumber(-11.1111)),
    (DecimalNumber(0), DecimalNumber(0)),
    (DecimalNumber(-5), DecimalNumber(5)),
    (DecimalNumber(44), DecimalNumber(-44)),
    (DecimalNumber(-5.22), DecimalNumber(5.22)),
    (DecimalNumber(44), -44)
]

int_data = [
    (DecimalNumber(11.1111), 11),
    (DecimalNumber(0), 0),
    (DecimalNumber(-5), -5),
    (DecimalNumber(44), 44),
    (DecimalNumber(-5.22), -5),
    (DecimalNumber(44), 44)
]

radd_data = [
    ([DecimalNumber(11)], DecimalNumber(11)),
    ([
         DecimalNumber(5.5),
         DecimalNumber(4.5),
         DecimalNumber(12)
     ],
        DecimalNumber(22)),
    ([
        DecimalNumber(-5.5),
        DecimalNumber(-4.5),
        DecimalNumber(-12)
     ],
        DecimalNumber(-22)),
    ((DecimalNumber(11), DecimalNumber(10)), DecimalNumber(21))
]
