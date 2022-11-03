import sys

SS_DIGITS = {
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

MIN_SEC_VALUES = (0, 15, 30, 45)
HOUR_VALUES = (0, 3, 6, 9)


def finger_placement(val, hour=False):
    try:
        return (HOUR_VALUES if hour else MIN_SEC_VALUES).index(val)
    except ValueError:
        return -1


def check_invalid(valid_positions, *positions):
    for position in positions:
        if position not in valid_positions:
            return False
    return True


def get_positions(h, m, s):
    return finger_placement(h, hour=True), finger_placement(m), finger_placement(s)


def t1(h, m, s):
    positions = get_positions(h, m, s)

    if not check_invalid((2, 3), *positions):
        return None

    unique_positions = set(positions)
    return 3 in unique_positions, 2 in unique_positions


def t2(h, m, s):
    positions = get_positions(h, m, s)

    if not check_invalid((0, 3), *positions):
        return None

    unique_positions = set(positions)
    return 0 in unique_positions, 3 in unique_positions


def t3(h, m, s):
    positions = get_positions(h, m, s)

    if not check_invalid((0, 1, 2), *positions):
        return None

    unique_positions = set(positions)
    return 2 in unique_positions, 0 in unique_positions, 1 in unique_positions


clock_data = []
for line in sys.stdin:
    # normalizace
    line = line.strip()
    if line == '---':
        break
    elif line == '-':
        clock_data = []
        continue
    time = line.strip().split(": ")[1]
    if time == 'broken':
        clock_data.append(None)
    else:
        time = time.split(':')
        # 24h to 12h shenanigans
        hour = int(time[0])
        if hour > 12:
            hour = hour - 12
        elif hour == 12:
            hour = 0
        clock_data.append((
            int(hour), int(time[1]), int(time[2])
        ))
    if len(clock_data) == 3:
        t1_result = t1(clock_data[0][0], clock_data[0][1], clock_data[0][2]) if clock_data[0] else (0, 0)
        t2_result = t2(clock_data[1][0], clock_data[1][1], clock_data[1][2]) if clock_data[1] else (0, 0)
        t3_result = t3(clock_data[2][0], clock_data[2][1], clock_data[2][2]) if clock_data[2] else (0, 0, 0)
        if None in (t1_result, t2_result, t3_result):
            print('#', end='')
            continue
        # noinspection PyTypeChecker
        final_number = list(SS_DIGITS.keys())[list(SS_DIGITS.values()).index((
            *t1_result,
            *t2_result,
            *t3_result
        ))]
        print(final_number, end='')
