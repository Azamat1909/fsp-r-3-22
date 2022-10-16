# Случайный надежный пароль.
# Используя решения из упражнений 100 и 102, напишите программу,
# генерирующую случайный надежный пароль и  выводящую его на экран.
gen_password = __import__('100')
check_for_reability = __import__('102')
m = 0
n = 0
while m != 1:
    x = gen_password.gen_password()
    c = check_for_reability.check_for_reability(x)
    if c == True:
        m += 1
    n += 1
    print(f'{x} - {c}')
print(f'С {n}-ой попытки удалось создать надёжный пароль')
