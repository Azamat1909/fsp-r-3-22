# Приоритеты операторов
# Напишите функцию с именем precedence, которая будет возвращать целое
# число, представляющее собой приоритет или старшинство математического оператора.
def precedence(a):
    if a == '+' or a == '-':
        return 1
    elif a == '*' or a == '/':
        return 2
    elif a == '^':
        return 3
    else:
        return -1


if __name__ == '__main__':
    operator = input('Enter mathematic operator: ')
    if precedence(operator) == -1:
        print('Error')
    else:
        print(precedence(operator))
