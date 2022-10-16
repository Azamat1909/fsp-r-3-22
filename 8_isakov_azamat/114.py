# Отрицательные, положительные и нули.Напишите программу, запрашивающую у пользователя целые числа, пока
# он не оставит строку ввода пустой. После окончания ввода на экран должны быть выведены сначала все
# отрицательные числа, которые были введены, затем нулевые и только после этого положительные.
neg_nums = []
zero = []
pos_nums = []

num = input('Enter nums (Enter for stop): ')
while num != '':
    if float(num) < 0:
        neg_nums.append(num)
    elif 1 > float(num) >= 0:
        zero.append(num)
    else:
        pos_nums.append(num)
    num = input('Enter nums (Enter for stop): ')

for i in neg_nums:
    print(i)
for j in zero:
    print(j)
for k in pos_nums:
    print(k)
