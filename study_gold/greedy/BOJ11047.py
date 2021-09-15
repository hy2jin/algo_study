# BOJ 11047 동전 0
import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]
ans = 0
for i in range(N-1, -1, -1):
    s, k = divmod(K, coin[i])
    if s:
        ans += s
        K = k
    if not K:
        break
print(ans)