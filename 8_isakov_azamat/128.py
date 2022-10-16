# Подсчитать элементы в списке
def countRange(ls, mn, mx):
    new_ls = sorted(ls)
    if mn in new_ls and mx in new_ls:
        new_ls1 = new_ls[new_ls.index(mn):new_ls.index(mx):]
        return len(new_ls1)
    elif mn in new_ls and mx not in new_ls:
        for i in range(len(new_ls)):
            if new_ls[i] > mx:
                mx = new_ls[i]
            else:
                mx = new_ls[len(new_ls) - 1]
                new_ls1 = new_ls[new_ls.index(mn):new_ls.index(mx) + 1:]
        return len(new_ls1)
    elif mn not in new_ls and mx in new_ls:
        new_ls1 = new_ls[:new_ls.index(mx):]
        return len(new_ls1)
    elif mn not in new_ls and mx not in new_ls or mn == 0:
        for i in range(len(new_ls)):
            if new_ls[i] <= mn:
                mn = new_ls[i]
            else:
                mn = new_ls[0]
            if new_ls[i] > mx:
                mx = new_ls[i]
            else:
                mx = new_ls[len(new_ls) - 1]
        new_ls1 = new_ls[new_ls.index(mn):new_ls.index(mx) + 1:]
        return len(new_ls1)


ls1 = [2, 3, 4, 6, 7, 8, 2, 2, 3]
# a = 0.01
# b = 3
# ls1 = [0.02, 0.4, 2.3, 4.5, 1.1, 5.2, 2, 2.2, 8]
# min_ls = min(ls1)
# min1 = min(min_ls, a, b)
# c = str(min1)
# d = c.index('.')
# abc = len(c[d + 1:])

# new_ls1 = []
# for x in ls1:
#     new_ls1.append(int(x * 10 ** abc))
# a = int(a * 10 ** abc)
# b = int(b * 10 ** abc)
print(countRange(ls1, 2, 7))
print(countRange(ls1, 1, 9))
print(countRange(ls1, 0, 8))
print(countRange(ls1, 0, 9))
