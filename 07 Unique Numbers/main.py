import sys

numbers = {}

for line in sys.stdin:
    for number in line.split(','):
        try:
            number = int(number)
            try:
                numbers[number] += 1
            except KeyError:
                numbers[number] = 1
        except ValueError:
            pass
print('all: ', end='')
print(*numbers.keys(), sep=',')
print('>1x: ', end='')
print(*[num for num, occurrences in numbers.items() if occurrences > 1], sep=',')
print('=1x: ', end='')
print(*[num for num, occurrences in numbers.items() if occurrences == 1], sep=',')
