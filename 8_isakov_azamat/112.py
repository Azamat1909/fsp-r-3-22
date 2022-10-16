# Удаляем выбросы. Напишите функцию, создающую копию списка с исключенными из него n наибольшими
# и наименьшими значениями и возвращающую ее в качестве результата.
def edit_list(l):
    list = l
    list.sort()
    list.pop(0)
    list.pop(len(list) - 1)
    return list


nums = []
num = input('Enter number (Enter for stop): ')
while num != '':
    nums.append(int(num))
    num = input('Enter number (Enter for stop): ')
if len(nums) < 4:
    print('Error')
else:
    print(f'{nums}\n{edit_list(nums)}')
