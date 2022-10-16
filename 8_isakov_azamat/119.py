# Ниже и выше среднего.
# Напишите программу, которая будет запрашивать у  пользователя числа, пока он не пропустит ввод. Сначала на экран должно быть выведено
# среднее значение введенного ряда чисел, после этого друг за другом необходимо вывести список чисел ниже среднего, равных ему(если такие
# найдутся) и выше среднего. Каждый список должен предваряться соответствующим заголовком.

num = input('Enter number (Enter for stop):')
nums = []
n_above_mid = []
num_middle = []
n_lower_mid = []
total = 0
while num != '':
    nums.append(int(num))
    num = input('Enter number (Enter for stop):')
for i in nums:
    total += i
mid = total / len(nums)
for x in nums:
    if x == mid:
        num_middle.append(x)
    elif x < mid:
        n_lower_mid.append(x)
    else:
        n_above_mid.append(x)
print(f'The average value of the numbers is {mid}')
print(
    f'List of numbers below average\n{n_lower_mid}:\nList of numbers equal to average\n{num_middle}\nList of numbers larger than average\n{n_above_mid}')
