from __future__ import annotations

import sys
from typing import Tuple

analog_translation = {
    0: (1, 1, 1, 1, 1, 1, 0),
    1: (0, 1, 1, 0, 0, 0, 0),
    2: (1, 1, 0, 1, 1, 0, 1),
    3: (1, 1, 1, 1, 0, 0, 1),
    4: (0, 1, 1, 0, 0, 1, 1),
    5: (1, 0, 1, 1, 0, 1, 1),
    6: (1, 0, 1, 1, 1, 1, 1),
    7: (1, 1, 1, 0, 0, 0, 0),
    8: (1, 1, 1, 1, 1, 1, 1),
    9: (1, 1, 1, 1, 0, 1, 1)
}

min_sec_position_values = (0, 15, 30, 45)
hour_position_values = (0, 3, 6, 9)


def only_valid(val, *args):
    for arg in args:
        if val != arg:
            return False
    return True


def finger_placement(val, hour=False):
    try:
        return (hour_position_values if hour else min_sec_position_values).index(val)
    except ValueError:
        return -1


def check_invalid(valid_positions, *positions):
    for position in positions:
        if position not in valid_positions:
            return False
    return True


def get_positions(h, m, s):
    return finger_placement(h, hour=True), finger_placement(m), finger_placement(s)


def t1(h, m, s) -> Tuple[bool, bool] | None:
    positions = get_positions(h, m, s)

    if not check_invalid((2, 3), *positions):
        return None

    unique_positions = set(positions)
    return 3 in unique_positions, 2 in unique_positions


def t2(h, m, s) -> Tuple[bool, bool] | None:
    positions = get_positions(h, m, s)

    if not check_invalid((0, 3), *positions):
        return None

    unique_positions = set(positions)
    return 0 in unique_positions, 3 in unique_positions


def t3(h, m, s) -> Tuple[bool, bool, bool] | None:
    positions = get_positions(h, m, s)

    if not check_invalid((0, 1, 2), *positions):
        return None

    unique_positions = set(positions)
    return 2 in unique_positions, 0 in unique_positions, 1 in unique_positions


t1_result = t1(6, 30, 45)
t2_result = t2(9, 0, 0)
t3_result = t3(0, 15, 0)
for num, analog in analog_translation.items():
    if analog == (*t1_result, *t2_result, *t3_result):
        print(num)
        break

# for line in sys.stdin:
#     if line == '---':
#         break
