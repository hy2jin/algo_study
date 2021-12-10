# BOJ 16928 뱀과 사다리 게임
import sys
from collections import deque
sys.stdin = open('16928.txt')
# input = sys.stdin.readline


def BFS():
    Q = deque([1])
    visited = [-1] * 101
    visited[1] = 0
    while Q:
        v = Q.popleft()
        if v == 100:
            return visited[100]

        for n in range(1, 7):
            nv = n + v
            if nv > 100:
                break
            if go[nv]:
                nv = go[nv]
            if visited[nv] == -1:
                visited[nv] = visited[v] + 1
                Q.append(nv)


N, M = map(int, input().split())
go = [0] * 101
for _ in range(N+M):
    n1, n2 = map(int, input().split())
    go[n1] = n2
print(BFS())