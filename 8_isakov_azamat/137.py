
def dice():
    from random import randint
    return randint(1, 6) + randint(1, 6)


D = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}

expected = {2: 1 / 36, 3: 2 / 36, 4: 3 / 36, 5: 4 / 36, 6: 5 / 36,
            7: 6 / 36, 8: 5 / 36, 9: 4 / 36, 10: 3 / 36, 11: 2 / 36, 12: 1 / 36}


for g in range(1000):
    i = dice()
    D[i] = D[i] + 1

for k in D:
    print(f'{k}\t|{D[k]/10:.2f}%\t|{expected[k] * 100:.2f}%')
