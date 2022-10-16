# Медиана трех значений.
def find_mediana(a, b, c):
    if a >= 0 and b >= 0 and c >= 0:
        # print(min(a, b, c), (a + b + c) - (min(a, b, c) + max(a, b, c)), max(a, b, c))
        print(f'Mediana = {(a + b + c) - (min(a, b, c) + max(a, b, c))}')


a = float(input('Enter firs number: '))
b = float(input('Enter second number: '))
c = float(input('Enter third number: '))

find_mediana(a, b, c)
