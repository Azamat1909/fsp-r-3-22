# Переводим целые числа в числительные. Написать программму, которая будет запрашивать число в диапазоне от 1 до 12 и выдавать его числительное.
numerals = ('first', 'second', 'third', 'fourth', 'fifth', 'sixth',
            'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth')


def find_numerals(num):
    return (numerals[num - 1])


if __name__ == "__main__":
    i = int(input('Enter number: '))
    if 0 < i <= 12:
        print(find_numerals(i))
