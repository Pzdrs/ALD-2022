import sys

for line in sys.stdin:
    def sanitize(string):
        return string.lower().strip()


    print('ano' if sanitize(line[::-1]) == sanitize(line) else 'ne')
