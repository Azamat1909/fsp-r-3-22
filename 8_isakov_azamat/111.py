# Обратный порядок. Напишите программу, которая, как и  в  предыдущем случае, будет запрашивать у
# пользователя целые числа и  сохранять их в  виде списка.
# Индикатором окончания ввода значений также должен служить ноль. На
# этот раз необходимо вывести на экран введенные значения в  порядке убывания.

nums = []
num = int(input('Enter number (\'0\' for stop): '))
while num != 0:
    nums.append(num)
    num = int(input('Enter number (\'0\' for stop): '))
nums.sort()
nums.reverse()
for i in nums:
    print(i)
