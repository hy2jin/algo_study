# BOJ2798 블랙잭
N, M = map(int, input().split())
cards = list(map(int, input().split()))

maxS = cards[0]
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            tmp = cards[i] + cards[j] + cards[k]
            if  tmp <= M and tmp > maxS:
                maxS = tmp
print(maxS)