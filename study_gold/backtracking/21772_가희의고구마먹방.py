# BOJ 21772 가희의 고구마 먹방
'''
G: 가희 / S: 고구마 / .: 빈칸 / #: 장애물
1초마다 상하좌우로 1칸 또는 그 자리에 머무른다
고구마가 있으면 먹는다. 먹는데 걸리는 시간은 없다
고구마를 최대한 많이 먹고싶다 ->  최대 몇개의 고구마를 먹을 수 있는지?
'''
import sys
sys.stdin = open('21772.txt')
# input = sys.stdin.readline


def recur(r, c, t, eat):
    global ans
    if ans == max_eat:
        return
    # # 남은 고구마랑 먹을수있는시간 합이 ans보다 작으면 그만 가도 됨 -> 이라고 생각했으나 아니였다. why?
    # if (max_eat - eat) + t < ans:
    #     return
    if t == 0:
        if eat > ans:
            ans = eat
        return

    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] != '#':
            if arr[nr][nc] == 'S':
                arr[nr][nc] = '.'
                recur(nr, nc, t-1, eat+1)
                arr[nr][nc] = 'S'
            else:
                recur(nr, nc, t-1, eat)
    recur(r, c, t-1, eat)


R, C, T = map(int, input().split())
max_eat = 0                 # 모든 고구마(S)의 수
arr = []
TF = False                  # 가희 좌표 찾으면 True, 가희 좌표는 (sr, sc)
for i in range(R):
    arr.append(list(input()))
    if not TF and 'G' in arr[i]:
        TF = True
        sr, sc = i, arr[i].index('G')
    max_eat += arr[i].count('S')
# print(arr)
# print(max_eat)
dr = [0, 1, 0, -1]       # 우, 하, 좌, 상
dc = [1, 0, -1, 0]
ans = 0
recur(sr, sc, T, 0)
print(ans)