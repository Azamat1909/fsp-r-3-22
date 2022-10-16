# Простое число?
# Напишите функцию для определения того, является ли введенное число простым.

def prime_num_def(a):
    c = True
    if a == 2:
        return c
    elif a > 2 and a % 2 == 0:
        return c == False
    else:
        for i in range(3, a):
            if a % i == 0:
                c = False
                break
        if c == True:
            return c
        else:
            c = False
            return c


if __name__ == '__main__':
    num = int(input('Enter number: '))
    if prime_num_def(num) == True:
        print(f'{num} is prime')
    else:
        print(f'{num} isn\'t prime')
