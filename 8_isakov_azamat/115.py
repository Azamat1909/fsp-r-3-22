# Список собственных делителей. Напишите функцию, которая будет возвращать список
# всех собственных делителей заданного числа.
def find_dividers(a):
    dividers = []
    for i in range(1, a):
        if a % i == 0:
            dividers.append(i)
    return dividers


if __name__ == '__main__':
    num = int(input('Enter number: '))
    print(find_dividers(num))
