# BOJ 16206 롤케이크
import sys
sys.stdin = open('input.txt')


N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
fi, la = [], []
for a in A:
    if a % 10: la += [a//10]
    else: fi += [a//10]

ans, cnt = 0, 0
if fi:
    for f in fi:
        ans += f
        cnt += f - 1
        if cnt >= M:
            print(ans) if cnt == M else print(ans - cnt + M - 1)
            exit()
if la:
    for l in la:
        ans += l
        cnt += l
        if cnt >= M:
            print(ans) if cnt == M else print(ans - cnt + M)
            exit()
print(ans)