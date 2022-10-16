

calendar = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def det_amount_days(m, y):
    if m > 12 or m < 1:
        return False
    elif y % 100 == 0 and y % 400 == 0 or y % 400 % 100 % 4 == 0:
        return calendar[m]
    elif m == 2:
        return 28
    else:
        return calendar[m]


if __name__ == '__main__':
    month = int(input('Enter month number: '))
    year = int(input('Enter year: '))
    print(det_amount_days(month, year))
