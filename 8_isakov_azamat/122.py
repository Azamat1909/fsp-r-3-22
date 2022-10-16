# «Поросячья латынь»
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
              'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
words = []

word = input('Enter word/sentence: ')

word = word.lower()
word = word.split()
for a in word:
    if a[0] == 't' and a[1] == 'h':
        a = a[2::] + a[0] + a[1] + 'ay'
        words.append(a)
        words.append(' ')
    elif a[0] in consonants:
        a = a[1::] + a[0] + 'ay'
        words.append(a)
        words.append(' ')
    else:
        a = a + 'way'
        words.append(a)
        words.append(' ')

print(''.join(words))
