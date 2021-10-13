# BOJ 1753 최단경로
import sys
from heapq import heappush, heappop         # 쓰는 것만 골라오기 heappush나 heappop을 하면 heapq로 생성됨
sys.stdin = open('1753.txt')


def dijkstra(K):
    visited[K] = 0
    heappush(heap, [0, K])                  # heappush(어디에, 무엇을)

    while heap:
        w, v = heappop(heap)                # heap에 있는 것들 중 w가 가장 작은게 pop 된다
        for nw, nv in adj[v]:               # v에서 갈 수 있는 곳들 중에서
            next = nw + w                   # v를 통해서 nv로 가는 가중치가
            if next < visited[nv]:          # 이미 구해진 nv로 가는 가중치보다 작으면 가중치 갱신
                visited[nv] = next
                heappush(heap, [next, nv])  # heap에 [가중치, 정점]을 push


V, E = map(int, input().split())
K = int(input())
INF = 1e9
adj = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())     # u에서 v로 가는데 가중치 w
    adj[u].append([w, v])                   # heap에서 가중치를 기준으로 정렬되기 위해서 가중치를 먼저 넣는다

heap = []
visited = [INF] * (V+1)
dijkstra(K)

for ans in visited[1:]:     # idx 0은 편의상 넣어준 것이니까 제외
    print(ans) if ans < INF else print('INF')
