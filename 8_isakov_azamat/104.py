# Шестнадцатеричные и десятичные числа.
# Напишите две функции с  именами hex2int и  int2hex для конвертации
# значений из шестнадцатеричной системы счисления(0, 1, 2, 3, 4, 5, 6, 7,
# 8, 9, A, B, C, D, E и F) в десятичную(по основанию 10) и обратно.
char = ('A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f')


def hex2int(a):
    return int(str(a), base=16)


def int2hex(b):
    return hex(int(b))


notation = int(
    input('\"1\" - for x16 --> x10\n\"2\" - for x10 --> x16\nEnter: '))
num = input('Enter number: ')


if notation == 1:
    if num in char or 9 > int(num) > 0:
        print(hex2int(num))
    else:
        print('Wrong input')
elif notation == 2:
    if 0 < int(num) < 16:
        print(int2hex(num)[2::].upper())
    else:
        print('Wrong input')
else:
    print('Wrong input')
