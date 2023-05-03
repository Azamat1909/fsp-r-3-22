index = input('Enter post index: ')
stat = {'A': 'Ньюфаундленд', 'B': 'Новая Шотландия', 'C': 'Остров Принца Эдуарда',
        'E': 'Нью-Брансуик', 'G': 'Квебек', 'H': 'Квебек',
        'J': 'Квебек', 'K': 'Онтарио', 'L': 'Онтарио',
        'M': 'Онтарио', 'N': 'Онтарио', 'P': 'Онтарио',
        'R': 'Манитоба', 'S': 'Саскачеван',
        'T': 'Альберта', 'V': 'Британская Колумбия',
        'X': 'Нунавут', 'X': 'Северо-Западные территории', 'Y': 'Юкон'}
index = index.upper()
if len(index) == 6 and index[1].isdigit() and index[3].isdigit() and index[5].isdigit() and index[0] in stat:
    if index[0] == 'X' and int(index[1]) == 0:
        print(
            f'Сельская местность {stat[index[0]]} или провинция Нунавут')
    elif index[0] == 'X' and int(index[1] > 0):
        print(
            f'Городская местность {stat[index[0]]} или провинция Нунавут')
    elif int(index[1]) > 0:
        print(f'Городская местность провинции {stat[index[0]]}')
    else:
        print(f'Сельская местность провинции {stat[index[0]]}')
else:
    print('Неверный индекс')
