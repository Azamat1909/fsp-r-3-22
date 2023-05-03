text = input('Enter text: ')
d = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
     'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
     'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...',
     'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
     '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
     '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}
res = []
for k in text.upper():
    if k in d:
        res.append(d[k])
print(' '.join(res))
