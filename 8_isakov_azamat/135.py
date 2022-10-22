# Решето Эратосфена
n = 100
prime = []
for i in range(n + 1):
    prime.append(i)
prime[0] = prime[1] = 0
p = 2
while p < n:
    if prime[p]:
        i = p + p
        while i <= n:
            prime[i] = 0
            i = i + p
    p += 1
for i in range(n + 1):
    if prime[i]:
        print(prime[i], end=' ')
