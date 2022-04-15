# BOJ 2531 회전초밥
import sys
sys.stdin = open('2531.txt')

N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]
sushi += sushi[:k-1]

ans = 0
for i in range(N):
    eat = set(sushi[i:i+k] + [c])
    ans = max(ans, len(eat))
print(ans)
