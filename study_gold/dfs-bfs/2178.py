# BOJ 2178 미로 탐색 (bfs)

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
q = [(0,0)]
visited[0][0] = 1
flag = False
while q:
    r, c = q.pop(0)
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] and not visited[nr][nc]:
            visited[nr][nc] = visited[r][c] + 1
            if nr == N-1 and nc == M-1:
                flag = True
                break
            else:
                q.append((nr, nc))
    if flag:
        break
print(visited[N-1][M-1])