# BOJ 1261 알고스팟
import sys
from heapq import heappop, heappush
sys.stdin = open('1261.txt')

C, R = map(int, input().split())
arr = [list(map(int, input())) for _ in range(R)]
visited = [[R*C]*C for _ in range(R)]   # 출발과 도착은 0이므로 R*C보다 무조건 작음
Q = []
heappush(Q, (0, 0, 0))                  # 시작 비용, 시작 좌표
visited[0][0] = 0                       # 0, 0에서 시작함, 비용은 0
dr = [-1, 1, 0, 0]                      # 상, 하, 좌, 우
dc = [0, 0, -1, 1]
while Q:
    cost, r, c = heappop(Q)
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        # 현재 위치에서 다음칸으로 가는게 비용이 더 적으면
        if 0 <= nr < R and 0 <= nc < C and cost + arr[nr][nc] < visited[nr][nc]:
            visited[nr][nc] = cost + arr[nr][nc]        # 갱신
            heappush(Q, (visited[nr][nc], nr, nc))
print(visited[-1][-1])
