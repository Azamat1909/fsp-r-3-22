# Случайные лотерейные номера.
# Напишите программу, которая будет случайным образом подбирать шесть номеров для вашего билета.
from random import randint
lot_ticket = []
c = 0
while c != 6:
    a = randint(1, 48)
    if a not in lot_ticket:
        lot_ticket.append(a)
        c += 1
lot_ticket.sort()
print(lot_ticket)
