# Форматирование списка.
# Обычно при написании перечислений и  списков мы разделяем их
# элементы запятыми, а перед последним ставим союз «и», как показано ниже:
# * яблоки
# * яблоки и апельсины
# * яблоки, апельсины и бананы
# * яблоки, апельсины, бананы и лимоны
# Напишите функцию, которая будет принимать на вход список из строк
# и возвращать собранную строку из его элементов в описанной выше манере.
# ----------------
# В основной программе запросите у пользователя несколько
# элементов списка, отформатируйте их должным образом при помощи
# функции и выведите на экран.

def format_the_list(a):
    b = a
    c = 0
    if len(a) != 1:
        b.insert(len(b) - 1, ' и ')
        while c < len(b) - 3:
            b.insert(1 + c, ', ')
            c += 2
        return ''.join(b)
    else:
        return ''.join(a)


list = []

word = input('Enter word (Enter for stop): ')
while word != '':
    list.append(word)
    word = input('Enter word (Enter for stop): ')
print(format_the_list(list))
