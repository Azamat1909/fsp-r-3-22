# Разбиение строки на лексемы
def tokenizing(a):
    ls = []
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbol = ['*', '/', '^', '-', '+', '(', ')']
    l = a
    l = list(l)
    l.append('-')
    x = ''
    for c in l:
        if c in num:
            x += c
        elif c in symbol:
            ls.append(x)
            ls.append(c)
            x = ''
        elif c == ' ':
            0
        else:
            ls.append(c)
            x = ''
        for s in range(len(ls)):
            if '' in ls:
                index = ls.index('')
                ls.pop(index)
    return ls[:len(ls) - 1:]


if __name__ == '__main__':
    char = input('Enter a mathematical expression: ')
    print(tokenizing(char))
