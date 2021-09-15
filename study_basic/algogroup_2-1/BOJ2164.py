# BOJ 2164 카드2

N = int(input())
card = list(range(1, N+1))
i = 0
while True:
    if len(card) == i:
        print(card[i-1])
        break
    i += 1
    if len(card) > i:
        card.append(card[i])
        i += 1
