# BOJ 1743 음식물 피하기
import sys
from collections import deque
sys.stdin = open('1743.txt')
# input = sys.stdin.readline


def BFS(r, c):
    Q = deque([[r, c]])
    size = 1
    while Q:
        i, j = Q.popleft()
        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:       # 상, 우, 하, 좌 순서로 확인
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj]:     # 쓰레기가 있으면
                arr[ni][nj] = 0     # 쓰레기 없애고
                Q.append([ni, nj])
                size += 1
    return size


N, M, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]

rc = []                     # 쓰레기 좌표 리스트
for _ in range(K):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1       # 쓰레기 있음 표시
    rc.append([r-1, c-1])   # 리스트에 담기

ans = 1
for r, c in rc:             # 리스트에서 좌표 하나씩 꺼내서
    if arr[r][c]:           # 거기에 쓰레기가 있으면
        arr[r][c] = 0       # 없애고
        size = BFS(r, c)    # BFS로 쓰레기 크기 조사
        if size > ans:      # 가장 큰 쓰레기 크기 갱신
            ans = size
print(ans)
