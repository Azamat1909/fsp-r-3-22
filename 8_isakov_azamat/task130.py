# Унарные и бинарные операторы
from task129 import tokenizing


def find_unary_sign(a):
    c = 0
    ls = a
    operator = ['*', '-', '+', '/', '(', '^']
    for i in ls:
        if i == '-':
            if ls[0] == i or ls[c - 1] in operator:
                ls.pop(c)
                ls.insert(c, 'u-')
        if i == '+':
            if ls[0] == i or ls[c - 1] in operator:
                ls.pop(c)
                ls.insert(c, 'u+')
        c += 1
    return ls


if __name__ == '__main__':
    expression = input('Enter the expression: ')
    un_operator = []
    if tokenizing(expression) == 'Error':
        print('Error')
    else:
        for i in find_unary_sign(tokenizing(expression)):
            if i == 'u-' or i == 'u+':
                un_operator.append(i)
        print(un_operator)
