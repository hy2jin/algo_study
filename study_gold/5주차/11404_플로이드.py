# BOJ 11404 플로이드
import sys
from heapq import heappush, heappop
sys.stdin = open('11404.txt')

INF = int(1e20)
n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append((c, b))
cost = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    heap = []
    heappush(heap, (0, i))
    cost[i][i] = 0
    while heap:
        w, v = heappop(heap)
        for nw, nv in adj[v]:
            next = nw + w
            if next < cost[i][nv]:
                cost[i][nv] = next
                heappush(heap, (next, nv))

    for j in range(1, n+1):
        if cost[i][j] == INF:
            cost[i][j] = 0

for i in range(1, n+1):
    print(*cost[i][1:])
