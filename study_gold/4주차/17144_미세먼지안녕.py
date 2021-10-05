# BOJ 17144 미세먼지 안녕!
import sys
sys.stdin = open('17144.txt')

# 상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def update():
    for r in range(N):
        for c in range(M):
            can_diffuse = 0                 # 몇번 확산
            if arr[r][c][0] >= 5:
                tmp = arr[r][c][0]//5       # 한번 확산
                for d in range(4):
                    nr, nc = r+dr[d], c+dc[d]
                    if 0 <= nr < N and 0 <= nc < M and arr[nr][nc][0] != -1:
                        can_diffuse += 1
            else:
                tmp = 0
            arr[r][c] = [arr[r][c][0] - can_diffuse*tmp, tmp]


def diffusion():
    for r in range(N):
        for c in range(M):
            if arr[r][c][1]:                # 확산될 먼지가 있으면
                for d in range(4):
                    nr, nc = r + dr[d], c + dc[d]
                    if 0 <= nr < N and 0 <= nc < M and arr[nr][nc][0] != -1:
                        arr[nr][nc][0] += arr[r][c][1]      # 확산될 수 있는곳에 확산


def purifier():
    dir = [
        [(0, 1), (-1, 0), (0, -1), (1, 0)],     # 위 (우, 상, 좌, 하)
        [(0, 1), (1, 0), (0, -1), (-1, 0)]      # 아래 (우, 하, 좌, 상)
    ]
    for f in range(2):
        r, c = cleaner[f]
        if f:       # 아래
            pz = 0
            count = [M-c-1, N-r-1, M-c-1, N-r-1]            # 몇번 밀지
            for i in range(4):
                cnt = count[i]
                while cnt > 0:
                    cnt -= 1
                    if arr[r][c][0] != -1:      # 공기청정기는 pass
                        arr[r][c][0], pz = pz, arr[r][c][0]
                    nr, nc = r+dir[f][i][0], c+dir[f][i][1]
                    r, c = nr, nc

        else:       # 위
            pz = 0
            count = [M-c-1, r, M-c-1, r]        # 몇번 밀지
            for i in range(4):
                cnt = count[i]
                while cnt > 0:
                    cnt -= 1
                    if arr[r][c][0] != -1:      # 공기청정기는 pass
                        arr[r][c][0], pz = pz, arr[r][c][0]
                    nr, nc = r+dir[f][i][0], c+dir[f][i][1]
                    r, c = nr, nc


N, M, T = map(int, input().split())     # N행 M열 / T초 후 방에 남아있는 미세먼지 양 출력
arr = []            # 방
cleaner = []        # 공기청정기 위치 (2개) / [(위쪽 좌표), (아래쪽 좌표)]

for i in range(N):
    arr.append(list(map(int, input().split())))
    for j in range(M):
        if arr[i][j] == -1:             # 공기청정기 위치
            cleaner.append((i, j))
        arr[i][j] = [arr[i][j], 0]      # (먼지 양, 확산될 양)

for t in range(T):
    update()
    diffusion()
    purifier()

ans = 0
for i in range(N):
    for j in range(M):
        ans += arr[i][j][0]
print(ans+2)    # 공기청정기 +2
