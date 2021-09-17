# BOJ 2468 안전영역 (dfs)
import sys
sys.stdin = open('2468.txt')
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def dfs(r, c):
    visited[r][c] = 1
    for j in range(4):
        nr, nc = r+dr[j], c+dc[j]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] - i > 0 and not visited[nr][nc]:
            visited[nr][nc] = 1
            dfs(nr, nc)


N = int(input())
arr = []
maxH = 0
for _ in range(N):
    tmp = list(map(int, input().split()))
    maxH = max(maxH, max(tmp))
    arr.append(tmp)

ans = 1
for i in range(1, maxH):
    cnt = 0
    visited = [[0] * N for _ in range(N)]
    for p in range(N):
        for q in range(N):
            if arr[p][q] - i > 0 and not visited[p][q]:
                cnt += 1
                dfs(p, q)
    ans = max(ans, cnt)

print(ans)