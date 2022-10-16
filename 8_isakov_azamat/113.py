# Избавляемся от дубликатов.
# На экране должны быть показаны слова, введенные пользователем, но без повторов, – каждое по одному разу.

words = []
word = input('Enter word (Enter for stop): ')
while word != '':
    if word not in words:
        words.append(word)
    word = input('Enter word (Enter for stop): ')
for char in words:
    print(char)
