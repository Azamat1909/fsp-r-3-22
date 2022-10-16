# Центрируем строку. Напишите функцию, которая будет принимать в  качестве параметров
# строку s, а также ширину окна в символах – w.
def center(s, w):
    if len(s) >= w:
        print(s)
    else:
        print(' ' * ((w - len(s)) // 2) + s)


center('hello', 7)
center('Azamat', 10)
center('Martin Luter King', 20)
