# tady jsem si nabidnul https://www.youtube.com/watch?v=3COJ95juomM&ab_channel=TanishqChaudhary
import sys


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def get_next_palindrome(n):
    if is_palindrome(n):
        n += 1
    if is_palindrome(n): return n
    digits = len(str(n))
    if digits == 1:
        return n + 1
    if digits % 2 == 0:
        # even
        left = str(n)[0:int(digits / 2)]
        right = str(n)[digits // 2::]
        if int(left[::-1]) > int(right):
            return int(left + left[::-1])
        else:
            left = str(int(left) + 1)
            return int(left + left[::-1])
    else:
        # odd
        left = str(n)[0:int(digits / 2)]
        middle = str(n)[int(digits / 2)]
        right = str(n)[int(digits / 2) + 1::]
        if int(left[::-1]) <= int(right) and int(middle) + 1 > 9:
            middle = 0
            left = str(int(left) + 1)
        elif int(left[::-1]) < int(right):
            middle = int(middle) + 1
        return int(left + str(middle) + left[::-1])


for line in sys.stdin:
    try:
        num = int(line)
        if num == -1:
            break
        print(get_next_palindrome(num))
    except ValueError:
        pass
