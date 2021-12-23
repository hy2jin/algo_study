# BOJ 1916 최소비용 구하기
import sys
from heapq import heappush, heappop
sys.stdin = open('1916.txt')


def dijkstra():
    Q = []
    visited[S] = 0                      # S에서 S로 가는 비용 0
    heappush(Q, (0, S))
    while Q:
        c, v = heappop(Q)
#########################################
        if visited[v] < c:
            continue
#########################################
        for nc, w in adj[v]:            # v에서 w로 가는 비용 nc
            if c + nc < visited[w]:     # 지금 경로에서 w로 가는 비용이 이미 구해져 있는 w로 가는 비용보다 작으면
                visited[w] = c + nc     # 갱신
                heappush(Q, (visited[w], w))
    return visited[E]


N = int(input())
M = int(input())
visited = [9876543210]*(N+1)
adj = [[] for _ in range(N+1)]

# a에서 b로 가는데 드는 비용: c
for _ in range(M):
    a, b, c = map(int, input().split())
    adj[a].append((c, b))

# S에서 E로 가는 최소 비용 구하기
S, E = map(int, input().split())
print(dijkstra())
