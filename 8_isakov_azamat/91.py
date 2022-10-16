# Григорианский календарь в порядковый. Функция должна возвращать порядковый номер заданного дня в указанном году.

def ordinalDate(d, m, y):
    calendar = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
                7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if m == 1:
        return d
    else:
        if y % 100 == 0 and y % 400 == 0 or y % 400 % 100 % 4 == 0:
            past_months = range(1, m)
            past_days = d
            for days in past_months:
                past_days += calendar[days]
            return past_days
        else:
            calendar = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
            past_months = range(1, m)
            past_days = d
            for days in past_months:
                past_days += calendar[days]
            return past_days


if __name__ == '__main__':
    day = int(input('Enter day: '))
    month = int(input('Enter month: '))
    year = int(input('Enter year: '))

    print(ordinalDate(day, month, year))
