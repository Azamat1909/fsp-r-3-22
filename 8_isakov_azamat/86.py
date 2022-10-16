# Плата за такси. Напишите функцию, принимающую в качестве единственного параметра расстояние поездки в километрах и возвращающую итоговую сумму оплаты такси. В  основной программе должен демонстрироваться результате вызова функции.
def find_price(l):
    service_taxi = 4
    sum = service_taxi + (l // 0.14 * 0.25)
    print(f'The price of the trip is ${sum}')


distance = float(input('Enter the distance (km): '))
find_price(distance)
