# BOJ 17070 파이프 옮기기 1
import sys
sys.stdin = open('17070.txt')
I = sys.stdin.readline


def move(r, c, d):      # d --> 0: 가로, 1: 대각선, 2: 세로
    global cnt
    if r == N-1 and c == N-1:
        cnt += 1
        return

    if d == 0:
        if c+1 < N and arr[r][c+1] == 0:
            move(r, c+1, d)
            if r+1 < N and arr[r+1][c+1] == 0 and arr[r+1][c] == 0:
                move(r+1, c+1, d+1)
    elif d == 1:
        if c+1 < N and arr[r][c+1] == 0:
            move(r, c+1, d-1)
        if r+1 < N and arr[r+1][c] == 0:
            move(r+1, c, d+1)
            if c+1 < N and arr[r+1][c+1] == 0 and arr[r][c+1] == 0:
                move(r+1, c+1, d)
    else:
        if r + 1 < N and arr[r + 1][c] == 0:
            move(r+1, c, d)
            if c+1 < N and arr[r+1][c+1] == 0 and arr[r][c+1] == 0:
                move(r+1, c+1, d-1)


N = int(I())            # 3이상 16이하, 집의 크기
arr = [list(map(int, I().split())) for _ in range(N)]
cnt = 0
move(0, 1, 0)           # 오른쪽 파이프 좌표, d --> 0: 가로, 1: 대각선, 2: 세로
print(cnt)
