# Линия наилучшего соответствия
X = []
Y = []

coor1 = input('Enter coordinate (x): ')

while coor1 != '':
    X.append(float(coor1))
    coor1 = input('Enter coordinate (x): ')
coor2 = input('Enter coordinate (y): ')
while len(Y) != len(X):
    Y.append(float(coor2))
    coor2 = input('Enter coordinate (y): ')
n = len(X)
sum_x = sum(X)
sum_y = sum(Y)
prod_xy = 0
square_x = 0
for i in range(len(X)):
    prod_xy += X[i] * Y[i]
    square_x += X[i] ** 2
m = (prod_xy - (sum_x * sum_y) / n) / (square_x - ((sum_x) ** 2) / n)
mid_x = sum_x / len(X)
mid_y = sum_y / len(Y)
b = mid_y - m * mid_x
print(f'y = {m:.2f}x + {b:.2f}')
