# BOJ 4963 섬의 개수
import sys
sys.stdin = open('4963.txt')
sys.setrecursionlimit(10**6)
dirs = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def dfs(i, j):
    for d in dirs:
        ni, nj = i+d[0], j+d[1]
        if 0 <= ni < h and 0 <= nj < w and arr[ni][nj]:
            arr[ni][nj] = 0
            dfs(ni, nj)


while True:
    w, h = map(int, input().split())        # h행 w열
    if w == h == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    for r in range(h):
        for c in range(w):
            if arr[r][c]:
                arr[r][c] = 0
                cnt += 1
                dfs(r, c)
    print(cnt)
