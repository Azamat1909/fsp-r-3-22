# Следующее простое число.
# В данном упражнении вам нужно написать функцию с именем nextPrime,
# которая находит и возвращает первое простое число, большее введенного
# числа n.

prime_num_def = __import__('98')


def nextPrime(b):
    b += 1
    while prime_num_def.prime_num_def(b) != True:
        b += 1
    return b


num = int(input('Enter number: '))
print(f'The next prime of the number {num} is {nextPrime(num)}')
