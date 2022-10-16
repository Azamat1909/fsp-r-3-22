# Тасуем колоду карт
def createDeck():
    nominal = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    suit = ['s', 'h', 'd', 'c']
    deck = []
    for s in suit:
        for n in nominal:
            card = str(n) + str(s)
            deck.append(card)
    return deck


def shuffle(list):
    from random import randint
    new_deck = list
    c = 0
    for i in range(52):
        x = randint(0 + c, 51)
        temp = new_deck[i]
        new_deck[i] = new_deck[x]
        new_deck[x] = temp
        c += 1
    return new_deck


if __name__ == '__main__':
    deck = createDeck()
    print(deck)
    print(shuffle(deck))
