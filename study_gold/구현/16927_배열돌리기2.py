# BOJ 16927 배열 돌리기2
import sys
sys.stdin = open('16927.txt')

# 하, 우, 상, 좌
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 아래로, 오른쪽으로, 위로, 왼쪽으로 몇번 옮길까?
move = [N-1, M-1, N-1, M-1]
for i in range(min(N, M) // 2):
    tmp = 2*(N + M) - (i*8) - 4
    for _ in range(R % tmp):
        r, c = i, i
        pz = arr[r][c]
        d = 0
        cnt = move[d]
        while True:
            nr, nc = r + dr[d], c + dc[d]
            arr[nr][nc], pz = pz, arr[nr][nc]
            r, c = nr, nc
            cnt -= 1
            if cnt == 0:
                d += 1
                if d == 4: break
                cnt = move[d]

    for m in range(4):
        move[m] -= 2

for a in arr:
    print(' '.join(map(str, a)))
