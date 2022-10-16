# Переводим меры.
# Напишите функцию, выражающую заданный объем ингредиентов с использованием минимально возможных замеров.
def measure(cups, tablespoons, teaspoons):
    teaspoon = teaspoons % 48 % 3
    tablespoon = (teaspoons // 3 + tablespoons) % 16
    t = (teaspoons // 3 + tablespoons) // 16
    cup = t + cups

    # return cup, tablespoon, teaspoon
    if cup > 1 and tablespoon > 1 and teaspoon > 1:
        return f'{cup} cups, {tablespoon} tablespoons, {teaspoon} teaspoons'
    elif cup <= 1 and tablespoon > 1 and teaspoon > 1:
        return f'{cup} cup, {tablespoon} tablespoons, {teaspoon} teaspoons'
    elif cup <= 1 and tablespoon <= 1 and teaspoon > 1:
        return f'{cup} cup, {tablespoon} tablespoon, {teaspoon} teaspoons'
    elif cup <= 1 and tablespoon <= 1 and teaspoon <= 1:
        return f'{cup} cup, {tablespoon} tablespoon, {teaspoon} teaspoon'
    elif cup > 1 and tablespoon <= 1 and teaspoon <= 1:
        return f'{cup} cups, {tablespoon} tablespoon, {teaspoon} teaspoon'
    elif cup > 1 and tablespoon > 1 and teaspoon <= 1:
        return f'{cup} cups, {tablespoon} tablespoons, {teaspoon} teaspoon'
    elif cup > 1 and tablespoon >= 1 and teaspoon > 1:
        return f'{cup} cups, {tablespoon} tablespoon, {teaspoon} teaspoons'
    elif cup <= 1 and tablespoon > 1 and teaspoon <= 1:
        return f'{cup} cup, {tablespoon} tablespoons, {teaspoon} teaspoon'


cup = int(input('Enter amount cup: '))
tablespoon = int(input('Enter amount tablespoons: '))
teaspoon = int(input('Enter amount teaspoons: '))
print(measure(cup, tablespoon, teaspoon))
