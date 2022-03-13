# BOJ 2668 숫자고르기
import sys
sys.stdin = open('2668.txt')
input = sys.stdin.readline

def recur(si):
    global ans
    if idx == num:
        ans = list(idx)
    if si == N:
        return
    for i in range(si, N+1):
        if i not in idx and data[i] not in num:
            idx.add(i)
            num.add(data[i])
            recur(i+1)
            idx.remove(i)
            num.remove(data[i])

N = int(input())
data = [0] + [int(input()) for _ in range(N)]
idx = set()
num = set()
ans = []
for i in range(1, N+1):
    idx.add(i)
    num.add(data[i])
    recur(i+1)
print(len(ans))
for an in ans:
    print(an)
