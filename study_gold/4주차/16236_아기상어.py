# BOJ 16236 아기 상어
import sys
from collections import deque
sys.stdin = open('16236.txt')

# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N = int(input())
arr = []
size = 2        # 상어 크기
want = size     # 상어가 자라기 위해 먹어야하는 물고기 수
fish = 0        # 물고기 몇마리? --> 다 먹으면 종료
time = 0
ans = time
for i in range(N):
    arr.append(list(map(int, input().split())))
    for j in range(N):
        if arr[i][j] == 9:
            shark = (i, j)      # 상어 위치
            arr[i][j] = 0       # 여기 지나다닐거니까 0으로
        elif arr[i][j]:
            fish += 1           # 물고기 몇마리?

q = deque()
q.append(shark)
visited = [[0]*N for _ in range(N)]
visited[shark[0]][shark[1]] = 1

while q and fish:
    can_go = []     # 갈 수 있는 곳
    can_eat = []    # 먹을 수 있는 곳

    # 한칸만 확인하기(q가 빌때까지) --> 만약 한칸에 갈곳이 없으면(=can_eat, can_go가 없으면) --> q가 비어서 바깥 while이 끝남 --> 아기상어의 엄마 호출(끝)
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr, nc = r+dr[d], c+dc[d]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if 0 < arr[nr][nc] < size:
                    can_eat.append((nr, nc))
                elif arr[nr][nc] == size or arr[nr][nc] == 0:
                    can_go.append((nr, nc))
                visited[nr][nc] = 1
    time += 1       # 한칸에 1초

    if can_eat:     # 먹을게 있으면 / 거리가 가장 가까운 물고기 먼저 먹는 것은 bfs이기 때문에 따로 생각해줄 필요 x
        can_eat.sort(key=lambda x:(x[0], x[1]))     # 행, 열 순으로 오름차순 정렬
        i, j = can_eat[0]       # 먹을게 많으면 가장 위에 있는 물고기, 가장 위에 여러마리면 가장 왼쪽 물고기 먹기
        q.append((i, j))        # 물고기 먹은 자리부터 다시 시작
        arr[i][j] = 0           # 먹었으니까 0
        visited = [[0]*N for _ in range(N)]
        visited[i][j] = 1       # 새로 시작하기 위한 visited 갱신

        fish -= 1
        want -= 1
        if not want:            # 원하는 만큼 물고기를 먹었으면
            size += 1           # 아기상어 성장
            want = size         # 원하는 물고기 갱신
        ans = time
    elif can_go:
        for go in can_go:
            q.append(go)

print(ans)
