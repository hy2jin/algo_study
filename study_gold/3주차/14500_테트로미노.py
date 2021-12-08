# BOJ 14500 테트로미노
import sys
sys.stdin = open('14500.txt')

# 우, 하, 좌, 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def dfs(r, c, cnt, v):
    global ans

    # 그냥 dfs로 하면 ㅏ모양을 계산할 수 없다 --> 3칸을 가면서 그때마다 갈수있는 좌표를 담아둔다
    lst = []
    for d in range(4):
        nr, nc = r+dr[d], c+dc[d]
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            lst.append((nr, nc))
    four[cnt] = lst

    if cnt == 3:                            # 3칸 왔으면
        # print('네번째 칸에 올수있는 좌표\n', four)
        for f in range(1, 4):
            for i, j in four[f]:
                if not visited[i][j]:       # 방문한적이 없는 위치가 4번째 자리
                    tmp = v + arr[i][j]     # 그 값 더해서 최대값 갱신
                    ans = max(ans, tmp)
        return

    # dfs
    for d in range(4):
        nr, nc = r+dr[d], c+dc[d]
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            visited[nr][nc] = 1
            dfs(nr, nc, cnt + 1, v + arr[nr][nc])
            visited[nr][nc] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
four = [[], [], [], []]
ans = 0
for r in range(N):
    for c in range(M):
        visited[r][c] = 1
        dfs(r, c, 1, arr[r][c])
        visited[r][c] = 0
print(ans)
