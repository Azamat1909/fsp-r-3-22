
# Список уже отсортирован?
def whetherSorted(ls):
    if len(ls) == 1:
        return 'Only 1 argument in list'
    elif len(ls) == 0:
        return '0 arguments in list'
    else:
        new_ls = []
        for i in ls:
            new_ls.append(i)
        new_ls.sort()
        new_ls_rev = new_ls[::-1]
        if new_ls == ls or new_ls_rev == ls:
            return True
        else:
            return False


list = []
num = input('Enter number (Enter for stop): ')
while num != '':
    list.append(int(num))
    num = input('Enter number (Enter for stop): ')

print(whetherSorted(list))
