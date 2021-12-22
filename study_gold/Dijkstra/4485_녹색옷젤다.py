# BOJ 4485 녹색 옷 입은 애가 젤다지?
import sys
from heapq import heappop, heappush
sys.stdin = open('4485.txt')


def dijkstra():
    Q = []
    heappush(Q, (arr[0][0], 0, 0))
    visited[0][0] = arr[0][0]
    while Q:
        cost, r, c = heappop(Q)
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            # 지금 위치에서 다음칸으로 가는게 다음칸으로 가는 최소 비용이면
            if 0 <= nr < N and 0 <= nc < N and cost+arr[nr][nc] < visited[nr][nc]:
                visited[nr][nc] = cost + arr[nr][nc]        # 최소 비용 갱신
                heappush(Q, (cost + arr[nr][nc], nr, nc))   # Q에 넣기
    return visited[-1][-1]


tc = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
while True:
    N = int(input())
    if N == 0:          # 0 받으면 반복문 그만
        break
    tc += 1             # 몇 번째 테스트케이스인지?
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[N*N*10]*N for _ in range(N)]        # 현재 좌표까지 드는 최소 비용을 저장
    print('Problem {}: {}'.format(tc, dijkstra()))
