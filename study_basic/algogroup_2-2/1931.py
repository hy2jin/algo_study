# BOJ 1931 회의실 배정
import sys
sys.stdin = open('1931.txt')
N = int(input())
se = [list(map(int, input().split())) for _ in range(N)]
se.sort(key=lambda x: (x[1], x[0]))
ans = 1
lst = se[0]
for i in range(1, N):
    if lst[-1] <= se[i][0]:
        lst += se[i]
        ans += 1
print(ans)