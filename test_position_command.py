import submarine_day2_part_1


def test_submarine_initialises_to_zero_horizontal():
    sub = submarine_day2_part_1.Submarine()
    assert sub.horizontal_position == 0


def test_submarine_forward():
    sub = submarine_day2_part_1.Submarine()
    sub.move(['forward', '2'])
    assert sub.horizontal_position == 2


def test_submarine_initialises_to_zero_horizontal_again():
    sub = submarine_day2_part_1.Submarine()
    assert sub.horizontal_position == 0


def test_submarine_initialises_to_zero_depth():
    sub = submarine_day2_part_1.Submarine()
    assert sub.depth == 0


def test_submarine_down():
    sub = submarine_day2_part_1.Submarine()
    sub.move(['down', '5'])
    assert sub.depth == 5


def test_submarine_up():
    sub = submarine_day2_part_1.Submarine()
    sub.move(['down', '5'])
    sub.move(['up', '3'])
    assert sub.depth == 2


