# BOJ 3190 뱀
import sys
sys.stdin = open('3190.txt')

# 우, 하, 좌, 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
d = 0

N = int(input())        # 보드의 크기
K = int(input())        # 사과의 개수
arr = [[0]*N for _ in range(N)]
for _ in range(K):
    i, j = map(int, input().split())
    arr[i-1][j-1] = 4   # 사과 위치 표시

L = int(input())        # 뱀의 방향 변환 횟수
turn = []
t = 0                   # turn의 idx
for l in range(L):
    turn.append(input().split())
    turn[l][0] = int(turn[l][0])

r, c = 0, 0             # 뱀 머리 위치 표시
arr[r][c] = 1
tail = [(r, c)]         # 지워야하는 꼬리의 좌표
l = 0                   # 꼬리 idx
X = 0
while True:
    X += 1
    nr, nc = r+dr[d], c+dc[d]
    if not (0 <= nr < N) or not (0 <= nc < N) or arr[nr][nc] == 1:
        break
    elif not arr[nr][nc]:           # 사과 안먹으면
        arr[tail[l][0]][tail[l][1]] = 0
        l += 1
    arr[nr][nc] = 1
    tail.append((nr, nc))

    if t < L and X == turn[t][0]:
        if turn[t][1] == 'L':       # L: 반시계
            d = (d-1) % 4
        else:                       # D: 시계
            d = (d+1) % 4
        t += 1
    r, c = nr, nc

print(X)
