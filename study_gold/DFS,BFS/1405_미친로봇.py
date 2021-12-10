# BOJ 1405 미친 로봇
import sys
sys.stdin = open('1405.txt')


def DFS(cnt, y, r, c):      # 남은 이동 횟수, 여기까지 올 확률, 현재 로봇 좌표
    global ans
    if cnt == 0:
        ans += y
        return

    for i in range(4):
        if EWSN[i]:                         # 이 방향으로 갈 확률이 0이면 갈 필요가 없다
            nr, nc = r+d[i][0], c+d[i][1]
            if not visited[nr][nc]:         # 경로가 단순하다 == 방문한곳에 또 방문하지 않는다
                visited[nr][nc] = 1
                DFS(cnt-1, y*EWSN[i], nr, nc)
                visited[nr][nc] = 0         # 다른 경로를 확인하기 위해 방문 흔적을 지운다


d = [(0, 1), (0, -1), (1, 0), (-1, 0)]      # 동서남북
EWSN = list(map(lambda x: 0.01*int(x), input().split()))
cnt = int(EWSN.pop(0) * 100)
visited = [[0] * (cnt*2+1) for _ in range(cnt*2+1)]
visited[cnt][cnt] = 1
ans = 0
DFS(cnt, 1, cnt, cnt)
print(ans)
