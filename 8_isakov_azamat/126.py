# Раздача карманных карт
from task125 import createDeck, shuffle


def deal(amount_players, amount_cards, n_deck):
    cards_for_players = []
    player_list = []
    for i in range(amount_players):
        c = 0
        while c != amount_cards:
            cards_for_players.append(n_deck[0])
            n_deck.pop(0)
            c += 1
    # n_deck = [n_deck]
    b = 0
    for a in range(amount_players):
        player_list.append(cards_for_players[b:b + amount_cards:])
        b += amount_cards
    return player_list, n_deck


deck = createDeck()
shuf = shuffle(deck)
amount_players = 4   # int(input('Enter amount players: '))
amount_cards = 5     # int(input('Enter amount cards: '))

players_list, positions = deal(amount_players, amount_cards, shuf)

for player_list in players_list:
    print(player_list)
print(positions)
# for position in positions:
#     print(position, end=' ')
