# Является ли строка целым числом?
# Написать функцию с именем isInteger, определяющую, представляет ли введенная строка целочисленное значение.
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def isinteger(a):
    a = a.strip()
    for i in a:
        if i not in nums:
            return f'{a} isn\'t integer'
    else:
        return f'{int(a)} is integer'


if __name__ == '__main__':
    num = input('Enter string: ')
    print(isinteger(num))
