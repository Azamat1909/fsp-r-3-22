# Расчет стоимости доставки. Напишите функцию, принимающую в качестве единственного параметра количество товаров в  заказе и  возвращающую общую сумму доставки.
def find_price(product_amount):
    if product_amount > 0:
        price = 10.95 + ((product_amount - 1) * 2.95)
        print(f'The price of the products is ${price:.2f}')
    else:
        print('Wrong input')


amount = int(input('Enter product amount: '))
find_price(amount)
