# Содержит ли список подмножество элементов?
# ------------------------------------------
# написать функцию isSublist, определяющую, является ли один список подсписком другого. На
# вход функции должны поступать два списка – larger и smaller. Функция
# должна возвращать значение True только в том случае, если список smaller
# является подсписком списка larger.
def isSublist(larger, smaller):
    b = 0
    end = len(smaller)
    if larger == smaller:
        return True
    else:
        while end != len(larger):
            x = larger[b: end] == smaller
            if x == True:
                return True
            else:
                b += 1
                end += 1
        return False


larger = [2, 4, 5, 6]
smaller = [4, 5]

print(isSublist(larger, smaller))
