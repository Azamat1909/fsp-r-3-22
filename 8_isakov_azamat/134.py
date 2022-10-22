# Все подсписки заданного списка
# ------------------------------
# Напишите функцию, возвращающую список, содержащий
# все возможные подсписки заданного. Например, в число
# подсписков списка [1, 2, 3] входят следующие: [], [1], [2], [3], [1, 2], [2, 3] и [1, 2, 3].

def def_all_subscriptions(list1: list):
    ls = []
    last_ls1 = []

    if len(list1) == 0:
        return []
    else:
        for num1 in range(len(list1)):
            for num2 in range(len(list1)):
                ls.append(list1[num1: num2 + 1])

    c = 1
    last_ls1.append([])
    while c < len(ls):
        for n in ls:
            if len(n) == c:
                last_ls1.append(n)
            else:
                continue
        c += 1

    return last_ls1


print(def_all_subscriptions([1, 2, 3]))
print(def_all_subscriptions([1, 2, 3, 4]))
print(def_all_subscriptions([1, 2, 3, 4, 5]))
