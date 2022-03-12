# BOJ 2667 단지번호붙이기
import sys
from collections import deque
sys.stdin = open('2667.txt')


def BFS(i, j):
    visited[i][j] = 1
    Q = deque([[i, j]])
    cnt = 1
    while Q:
        r, c = Q.popleft()
        for d in di:
            nr, nc = r+d[0], c+d[1]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == '1' and not visited[nr][nc]:
                visited[nr][nc] = 1
                Q.append([nr, nc])
                cnt += 1
    return cnt


N = int(input())
arr = [input() for _ in range(N)]
visited = [[0] * N for _ in range(N)]
di = [(1, 0), (-1, 0), (0, 1), (0, -1)]
town = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == '1' and not visited[i][j]:
            c = BFS(i, j)
            town.append(c)

print(len(town))
for tow in sorted(town):
    print(tow)
