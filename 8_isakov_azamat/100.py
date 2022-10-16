# Случайный пароль.
# Напишите функцию, которая будет генерировать случайный пароль.
from random import randint


def gen_password():
    c = 0
    password = []
    r = randint(7, 10)
    while c != r:
        a = randint(33, 125)
        password.append(chr(a))
        c += 1
    x = ''.join(password)
    return x


if __name__ == '__main__':
    print(gen_password())
