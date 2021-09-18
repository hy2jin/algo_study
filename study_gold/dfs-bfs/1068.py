# BOJ 1068 트리 (dfs)
import sys
sys.stdin = open('1068.txt')


def dfs(v):
    global cnt
    for w in adj[v]:
        if not visited[w]:
            visited[w] = 1
            dfs(w)
            if not adj[w]:
                cnt += 1


N = int(input())
pa = list(map(int, input().split()))
d = [int(input())]
print(pa)

adj = [[] for _ in range(N)]
for i in range(N):
    if pa[i] == -1:
        s = i
        continue
    if pa[i] in d:
        d.append(i)
    elif i not in d:
        adj[pa[i]].append(i)
print(adj)
cnt = 0
visited = [0] * N
visited[0] = 1
dfs(s)
print(cnt)