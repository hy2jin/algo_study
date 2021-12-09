# BOJ 1743 음식물 피하기
import sys
from collections import deque
sys.stdin = open('1743.txt')
# input = sys.stdin.readline


def BFS(r, c):
    Q = deque([[r, c]])
    visited[r][c] = 1
    size = 1
    while Q:
        i, j = Q.popleft()
        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:  # 상, 우, 하, 좌
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] and not visited[ni][nj]:
                visited[ni][nj] = 1
                Q.append([ni, nj])
                size += 1
    return size


N, M, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]

rc = []
for _ in range(K):
    r, c = map(int,input().split())
    arr[r-1][c-1] = 1
    rc.append([r-1, c-1])

ans = 1
for r, c in rc:
    if not visited[r][c]:
        size = BFS(r, c)
        if size > ans:
            ans = size
print(ans)
