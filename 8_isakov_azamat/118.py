# Словесные палиндромы.
# Напишите программу, которая будет запрашивать строку у пользователя и оповещать его о том, является ли она
# словесным палиндромом. Не забывайте игнорировать знаки препинания при выявлении результата.
words = []

sentence = input('Enter sentence: ')
sentence = sentence.lower()
punct_marks = ['!', ',', '.', '?', '-', ':', ';']
for x in sentence:
    if x not in punct_marks:
        words.append(x)

words = ''.join(words)
words = words.split()
new_words = words[::-1]
words = ''.join(words)
new_words = ''.join(new_words)
if words == new_words:
    print(f'The sentence is word phalindrome')
else:
    print('The sentence isn\'t word phalindrome')
