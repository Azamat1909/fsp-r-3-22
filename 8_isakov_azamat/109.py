# Магические даты.
# Напишите функцию, определяющую, является ли введенная дата магической.
# Используйте написанную функцию в  главной программе для отображения всех магических дат в XX веке.
det_amount_days = __import__('106')


def find_magic_date(d, m, y):
    x = m * d
    i = str(y)[-2::]
    if x == int(i):
        return 'Magic date'
    else:
        return 'Not magic date'


y = 1901
while y < 2000:
    for month in range(1, 13):
        i = det_amount_days.det_amount_days(month, y)
        for x in range(1, i + 1):
            res = find_magic_date(x, month, y)
            if res == 'Magic date':
                print(f'{x:02d}.{month:02d}.{y} - {res}')
    y += 1
