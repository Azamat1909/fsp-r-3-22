# Произвольные системы счисления.
# Напишите программу, которая позволит пользователю преобразовывать
# числа из одной системы счисления в другую произвольным образом.
def notion_to_dec(a, b):
    if b > 16 or b < 2:
        return 'Error'
    else:
        x = int(str(a), base=b)
        return x


def dec_to_notion(a, b):
    r = []
    if b == 2:
        return bin(a)[2::].upper()
    elif b == 8:
        return oct(a)[2::].upper()
    elif b == 16:
        return hex(a)[2::].upper()
    elif b > 10:
        while a >= b:
            c = a % b
            if c == 10:
                r.append('A')
            elif c == 11:
                r.append('B')
            elif c == 12:
                r.append('C')
            elif c == 13:
                r.append('D')
            elif c == 14:
                r.append('E')
            else:
                r.append(str(c))
            a //= b
        if a == 10:
            r.append('A')
        elif a == 11:
            r.append('B')
        elif a == 12:
            r.append('C')
        elif a == 13:
            r.append('D')
        elif a == 14:
            r.append('E')
        else:
            r.append(str(a))
        rest = ''.join(r[::-1])
        return rest
    else:
        while a >= b:
            c = a % b
            r.append(str(c))
            a //= b
        r.append(str(a))
        rest = ''.join(r[::-1])
        return rest


orig_n_s = int(input('Enter original number system: '))
target_n_s = int(input('Enter target number system: '))
num = int(input('Enter number: '))
print(dec_to_notion(notion_to_dec(num, orig_n_s), target_n_s))
