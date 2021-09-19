# BOJ 1012 유기농 배추
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
for _ in range(int(input())):
    M, N, K = map(int, input().split())     # N행, M열, 배추 K개
    arr = [[0]*M for _ in range(N)]
    bc = []
    for k in range(K):
        c, r = map(int, input().split())
        arr[r][c] = 1
        bc.append((r, c))
    # bfs
    cnt = 0
    for i, j in bc:
        if arr[i][j]:
            arr[i][j] = 0
            q = [(i, j)]
            cnt += 1
            while q:
                r, c = q.pop(0)
                for d in range(4):
                    nr, nc = r+dr[d], c+dc[d]
                    if 0 <= nr < N and 0 <= nc < M and arr[nr][nc]:
                        arr[nr][nc] = 0
                        q.append((nr, nc))
    print(cnt)