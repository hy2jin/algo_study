# BOJ 15685 드래곤 커브
import sys
# input = sys.stdin.readline
sys.stdin = open('15685.txt')

N = int(input())
arr = [[0] * 101 for _ in range(101)]
# 0: 우, 1: 상, 2: 좌, 3: 하
g_arr = [[0], [0, 1], [0, 1, 2, 1], [0, 1, 2, 1, 2, 3, 2, 1]]
for i in range(4, 11):
    tmp = g_arr[i-1] + list(map(lambda x: (x+1) % 4, g_arr[i-1][::-1]))
    g_arr.append(tmp)
# print(g_arr)

dr = [0, -1, 0, 1]      # 우, 상, 좌, 하
dc = [1, 0, -1, 0]
for _ in range(N):
    c, r, d, g = map(int, input().split())
    arr[r][c] = 1
    g_lst = g_arr[g]
    for j in g_lst:
        j = (j + d) % 4
        r, c = r + dr[j], c + dc[j]
        arr[r][c] = 1

cnt = 0
for r in range(100):
    for c in range(100):
        if arr[r][c] + arr[r][c+1] + arr[r+1][c] + arr[r+1][c+1] == 4:
            cnt += 1
print(cnt)
