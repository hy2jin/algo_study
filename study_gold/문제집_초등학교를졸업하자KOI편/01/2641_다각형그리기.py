# BOJ 2641 다각형그리기
import sys
from collections import deque
sys.stdin = open('2641.txt')

def roll(data):
    # 정방향 회전
    Q = deque(data)
    for _ in range(N):
        Q.rotate(1)
        if list(Q) == basic:
            return 1
    # 역방향 회전
    tmp = list(map(lambda x:dic[x], data[::-1]))
    Q = deque(tmp)
    for _ in range(N):
        Q.rotate(1)
        if list(Q) == basic:
            return 1


N = int(input())
basic = list(input().split())
M = int(input())
datas = [list(input().split()) for _ in range(M)]

dic = {'1': '3', '2': '4', '3': '1', '4': '2'}
idx = []
for i in range(M):
    find = roll(datas[i])
    if find:
        idx.append(i)

print(len(idx))
for j in idx:
    print(*datas[j])