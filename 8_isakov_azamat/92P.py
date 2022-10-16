# Порядковая дата в григорианский календарь.
# Разработайте функцию, принимающую в  качестве единственного
# параметра порядковую дату, включающую в  себя год и  день по порядку.

def find_date(d, y):
    calendar = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
                7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    m = 1
    num = range(1, 12)
    if d > 31:
        if y % 100 == 0 and y % 400 == 0 or y % 400 % 100 % 4 == 0:
            for i in num:
                if d <= 31:
                    break
                d -= calendar[i]
                m += 1
            return d, m
        else:
            calendar = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
            for i in num:
                if d <= 31:
                    break
                d -= calendar[i]
                m += 1
            return d, m
    else:
        return m == 1, d == d


date_num = int(input('Enter date number: '))


print(find_date(81, 2022))
