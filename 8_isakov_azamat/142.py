text = input('Enter text: ')
d = {}

for l in text:
    if l in d:
        d[l] += 1
    else:
        d[l] = 0

print(len(d))
