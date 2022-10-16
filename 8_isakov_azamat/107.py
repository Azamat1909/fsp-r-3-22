

def faction_reducer(n, m):
    if m > n:
        d = n
    elif m < n:
        d = m
    while n % d != 0 or m % d != 0:
        d -= 1
    n //= d
    m //= d
    return f'{n} / {m}'


a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
print(faction_reducer(a, b))
