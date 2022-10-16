# Озаглавим буквы. Создайте функцию, которая будет принимать
# на вход исходную строку и возвращать строку с восстановленными заглавными буквами.
def correct(s):
    c = 0
    str = []
    s = s.lower()
    s = s.capitalize()
    for w in s:
        if c >= 1:
            str.append(w.upper())
            c = 0
        elif w == '!' or '?' == w or '.' == w:
            c += 1
            str.append(w)
        else:
            c = 0
            str.append(w)

    res = ''.join(str)
    x = res.replace(' i ', ' I ')
    return x


str = input('Enter string: ')
print(correct(str))
