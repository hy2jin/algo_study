# BOJ 15686 치킨 배달
import sys
sys.stdin = open('15686.txt')

from itertools import combinations
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, M = map(int, input().split())        # NxN행렬, M개의 치킨집만 운영
arr = []            # 도시 정보
one = 0             # 집 수
two = []            # 치킨집 좌표
for i in range(N):
    arr.append(list(map(int, input().split())))
    for j in range(N):
        if arr[i][j] == 2:
            two.append((i, j))
        elif arr[i][j] == 1:
            one += 1
chicken = combinations(two, M)          # M개의 치킨집 좌표 조합

min_ans = 987654321     # 적당히 큰 값
for chi in chicken:     # 치킨집 좌표 조합 모든걸 확인해야함
    check = one         # 모든 집 찾으면 그만
    ans = 0             # 치킨집 - 집 거리의 합
    Q = deque()
    visited = [[-1]*N for _ in range(N)]
    for ch in chi:      # 좌표 한번에 넣을 방법이 이것뿐인가..?
        Q.append(ch)
        visited[ch[0]][ch[1]] = 0

    while Q:
        r, c = Q.popleft()
        for d in range(4):
            nr, nc = r+dr[d], c+dc[d]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == -1:
                visited[nr][nc] = visited[r][c] + 1
                Q.append((nr, nc))
                if arr[nr][nc] == 1:
                    ans += visited[nr][nc]
                    check -= 1
        if not check:
            break
    if ans < min_ans:
        min_ans = ans

print(min_ans)
