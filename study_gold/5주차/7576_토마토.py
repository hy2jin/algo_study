# BOJ 7576 토마토
import sys
from collections import deque
sys.stdin = open('7576.txt')

M, N = map(int, input().split())
arr = []
nope = 0
tomato = []                             # 다 익은 토마토 시작
for i in range(N):
    arr.append(list(map(int, input().split())))
    for j in range(M):
        if arr[i][j] == -1:             # 빈 칸
            nope += 1
        elif arr[i][j]:                 # 익은 토마토 있는 칸
            nope += 1
            tomato.append((i, j, 0))
cnt = M * N - nope                      # 익혀야 하는 토마토 수

if cnt == 0:
    print(0)
    exit()

q = deque()
for tmt in tomato:
    q.append(tmt)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
ans = 0
while q:
    r, c, t = q.popleft()
    for d in range(4):
        nr, nc = r+dr[d], c+dc[d]
        if 0 <= nr < N and 0 <= nc < M and not arr[nr][nc]:
            arr[nr][nc] = 1
            q.append((nr, nc, t+1))
            cnt -= 1
            if t+1 > ans:
                ans = t+1

print(-1) if cnt else print(ans)        # 익혀야 할 토마토가 남아있으면 -1 출력
