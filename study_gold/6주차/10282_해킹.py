# BOJ 10282 해킹
import sys
from heapq import heappush, heappop
sys.stdin = open('10282.txt')
INF = int(1e20)


def dijkstra(num):
    Q = []
    heappush(Q, (0, num))
    visited = [INF] * (n+1)
    visited[num] = 0
    while Q:
        t, v = heappop(Q)
        for nt, nv in adj[v]:
            if nt + t < visited[nv]:
                visited[nv] = nt + t
                heappush(Q, (nt + t, nv))
    return visited


for _ in range(int(input())):
    n, d, c = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        adj[b].append([s, a])       # b가 감염되면 s초 후 a도 감염
    time = dijkstra(c)
    cnt = sec = 0
    for i in range(n+1):
        if time[i] < INF:
            cnt += 1                # 감염된 컴퓨터 수
            if sec < time[i]:
                sec = time[i]       # 제일 오래 걸린 시간
    print(cnt, sec)
