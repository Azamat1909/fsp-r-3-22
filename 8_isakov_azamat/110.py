# Порядок сортировки. Напишите программу, которая будет запрашивать у пользователя целочисленные значения и сохранять их в виде списка.
nums = []
num = int(input('Enter number (\'0\' for stop): '))
while num != 0:
    nums.append(num)
    num = int(input('Enter number (\'0\' for stop): '))
nums.sort()
for i in nums:
    print(i)
