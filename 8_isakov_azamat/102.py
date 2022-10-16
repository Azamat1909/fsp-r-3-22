# Проверка пароля на надежность
LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def check_for_reability(s):
    a = 0
    b = 0
    c = 0
    if len(s) < 8:
        return False
    else:
        for l in s:
            if l in LETTERS:
                a += 1
            elif l in letters:
                b += 1
            elif l in nums:
                c += 1
        if a > 0 and b > 0 and c > 0:
            return True
        else:
            return False


if __name__ == '__main__':
    password = input('Enter password: ')
    if check_for_reability(password) == True:
        print(f'The password is strong')
    else:
        print(f'The password isn\'t strong')
