# Случайный номерной знак.
# Напишите функцию, которая будет генерировать случайный номерной знак.
from random import randint


def plate_num():
    c = 0
    x = randint(1, 2)
    plate = []
    if x == 1:
        while c != 4:
            plate.append(str(randint(0, 9)))
            c += 1
        c = 0
        while c != 3:
            plate.append(chr(randint(65, 90)))
            c += 1
    else:
        while c != 3:
            plate.append(chr(randint(65, 90)))
            c += 1
        c = 0
        while c != 3:
            plate.append(str(randint(0, 9)))
            c += 1
    res = ''.join(plate)
    return res


print(plate_num())
