# BOJ 2206 벽 부수고 이동하기
import sys
from collections import deque
# input = sys.stdin.readline
sys.stdin = open('2206.txt')

dr = [0, 1, 0, -1]      # 우, 하, 좌, 상
dc = [1, 0, -1, 0]

N, M = map(int, input().strip().split())
arr = [list(map(int, input().strip())) for _ in range(N)]
# [0, 0]: [벽을 부수고 찾아온 거리, 벽을 안부수고 찾아온 거리]
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]

# 좌표(r,c), canBreak(벽을 부술 수 있는가?)
Q = deque([[0, 0, 1]])
visited[0][0][1] = 1

while Q:
    r, c, canBreak = Q.popleft()
    for d in range(4):
        nr, nc = r+dr[d], c+dc[d]
        # 새로 방문하는게 더 멀지 않으면 최단경로일 가능성이 있음
        if 0 <= nr < N and 0 <= nc < M:
            # 벽이 아니면 그대로 ㄱㄱ
            if not arr[nr][nc] and not visited[nr][nc][canBreak]:
                visited[nr][nc][canBreak] = visited[r][c][canBreak] + 1
                Q.append([nr, nc, canBreak])
            # 벽인데 부술 수 있으면 부수고 ㄱㄱ --> 부쉈으니까 앞으로는 idx 0에 표시해야함
            elif arr[nr][nc] and canBreak and not visited[nr][nc][0]:
                visited[nr][nc][0] = visited[r][c][canBreak] + 1
                Q.append([nr, nc, 0])

# 마지막 행렬에 도착했을때 거리가 작은 게 m, 큰게 M --> m이 0이면 M이 최단거리 --> M도 0이면 -1 출력
m, M = visited[-1][-1] if visited[-1][-1][0] < visited[-1][-1][1] else visited[-1][-1][::-1]
ans = m if m else M
print(ans) if ans else print(-1)
