# Совершенные числа. Напишите функцию для определения того, является ли заданное число совершенным.
dividers = __import__('115')


def find_perfect_num(a):
    res = 0
    for i in dividers.find_dividers(a):
        res += i
    if res == a:
        return True
    else:
        return False


a = range(1, 10001)
for b in a:
    c = find_perfect_num(b)
    if c == False:
        0
    else:
        print(f'{b} is ideal')
