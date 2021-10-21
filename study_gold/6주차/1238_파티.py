# BOJ 1238 파티
import sys
from heapq import heappush, heappop
sys.stdin = open('1238.txt')
INF = int(1e20)


def dijkstra(n, TF):
    time = [INF] * (N+1)                    # n에서 idx로 가는데걸리는 최단 시간
    time[n] = 0
    Q = []
    heappush(Q, (0, n))
    if TF:
        while Q:
            t, v = heappop(Q)
            for nt, nv in adj[v]:
                if nt + t < time[nv]:
                    time[nv] = nt + t
                    heappush(Q, (nt + t, nv))
    else:
        while Q:
            t, v = heappop(Q)
            for nt, nv in reverse_adj[v]:
                if nt + t < time[nv]:
                    time[nv] = nt + t
                    heappush(Q, (nt + t, nv))
    for j in range(1, N+1):
        if time[j] == INF:
            time[j] = 0
    return time

N, M, X = map(int, input().split())
adj = [[] for _ in range(N+1)]
reverse_adj = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    adj[a].append([c, b])                   # a에서 b로 가는데 c 시간
    reverse_adj[b].append([c, a])

to_X = dijkstra(X, 1)
from_X = dijkstra(X, 0)

ans = 0
for i in range(1, N+1):
    if i != X:
        tmp = to_X[i] + from_X[i]
        if tmp > ans:
            ans = tmp
print(ans)
