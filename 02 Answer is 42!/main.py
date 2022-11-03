import sys

for line in sys.stdin:
    try:
        number = int(line)
        if number == 42: break
        print(number)
    except ValueError:
        pass
