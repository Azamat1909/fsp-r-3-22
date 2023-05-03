word1 = input('Enter first word: ')
word2 = input('Enter second word: ')
c = 0
d1 = {}
for l in word1:
    d1[l] = 0
for i in word2:
    if i in d1:
        d1[i] += 1
    else:
        d1[i] = 0
for i in d1.values():
    c += i

if c == len(word1):
    print('Анаграммы')
else:
    print('Не аннаграммы')
