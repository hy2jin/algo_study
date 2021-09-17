# BOJ 2644 촌수계산 (dfs)

import sys
sys.stdin = open('2644.txt')


def dfs(v):
    if v == e:
        return
    for w in adj[v]:
        if visited[w] == -1:
            visited[w] = visited[v] + 1
            dfs(w)


n = int(input())
s, e = map(int, input().split())
m = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)
visited = [-1] * (n+1)
visited[s] = 0
dfs(s)
print(visited[e])