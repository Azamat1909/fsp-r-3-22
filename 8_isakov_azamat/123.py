# «Поросячья латынь» (продолжение).
# Расширьте свое решение упражнения 122, чтобы ваш анализатор корректно
# обрабатывал символы в верхнем регистре и знаки препинания, такие
# как запятая, точка, а также восклицательный и  вопросительный знаки.
# Если в оригинале слово начинается с заглавной буквы, то в переводе на
# «поросячью латынь» оно также должно начинаться с  заглавной буквы,
# тогда как буквы, перенесенные в конец слов, должны стать строчными.
# Например, слово Computer должно быть преобразовано в Omputercay. Если
# в конце слова стоит знак препинания, он там же и должен остаться после
# выполнения перевода. То есть слово в конце предложения Science! необходимо трансформировать в Iencescay!.
VOWELS = ('A', 'E', 'I', 'O', 'U')
CONSONANTS = ('B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M',
              'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z')
vowels = ('a', 'e', 'i', 'o', 'u')
consonants = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
              'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')
punct_marks = ['!', ',', '.', '?', '-', ':', ';']
words = []
word = input('Enter word/sentence: ')
word = word.split()
for a in word:
    if a[len(a) - 1] in punct_marks:
        m = punct_marks.index(a[len(a) - 1])
    # print(a[len(a) - 1])
    if a[0] == 't' and a[1] == 'h' and a[len(a) - 1] in punct_marks:
        a = a[2:len(a) - 1:] + a[0] + a[1] + 'ay' + punct_marks[m]
        words.append(a)
        words.append(' ')
    elif a[0] in consonants and a[len(a) - 1] in punct_marks:
        a = a[1:len(a) - 1:] + a[0] + 'ay' + punct_marks[m]
        words.append(a)
        words.append(' ')
    elif a[0] in vowels and a[len(a) - 1] in punct_marks:
        a = a[:len(a) - 1:] + 'way' + punct_marks[m]
        words.append(a)
        words.append(' ')
    elif a[0] == 'T' and a[1] == 'h' and a[len(a) - 1] in punct_marks:
        a = a.lower()
        a = a[2:len(a) - 1:] + a[0] + a[1] + 'ay' + punct_marks[m]
        a = a.capitalize()
        words.append(a)
        words.append(' ')
    elif a[0] in CONSONANTS and a[len(a) - 1] in punct_marks:
        a = a.lower()
        a = a[1:len(a) - 1:] + a[0] + 'ay' + punct_marks[m]
        a = a.capitalize()
        words.append(a)
        words.append(' ')
    elif a[0] in VOWELS and a[len(a) - 1] in punct_marks:
        a = a.lower()
        a = a[1:len(a) - 1:] + a[0] + 'ay' + punct_marks[m]
        a = a.capitalize()
        words.append(a)
        words.append(' ')
    elif a[0] == 'T' and a[1] == 'h':
        a = a.lower()
        a = a[2::] + a[0] + a[1] + 'ay'
        a = a.capitalize()
        words.append(a)
        words.append(' ')
    elif a[0] in CONSONANTS:
        a = a.lower()
        a = a[1::] + a[0] + 'ay'
        a = a.capitalize()
        words.append(a)
        words.append(' ')
    elif a[0] in VOWELS:
        a = a.lower()
        a = a[1::] + a[0] + 'ay'
        a = a.capitalize()
        words.append(a)
        words.append(' ')
    elif a[0] == 't' and a[1] == 'h':
        a = a[2::] + a[0] + a[1] + 'ay'
        words.append(a)
        words.append(' ')
    elif a[0] in consonants:
        a = a[1::] + a[0] + 'ay'
        words.append(a)
        words.append(' ')
    elif a[0] in vowels:
        a = a + 'way'
        words.append(a)
        words.append(' ')
words = ''.join(words)
words = words[:len(words) - 1:]
print(words)
