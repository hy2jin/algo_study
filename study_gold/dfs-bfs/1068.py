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

adj = [[] for _ in range(N)]
for i in range(N):
    if pa[i] in d:
        d.append(i)
    elif pa[i] != -1 and i not in d and pa[i] not in d:
        adj[pa[i]].append(i)

cnt = 0
visited = [0] * N
visited[0] = 1
dfs(0)
print(cnt)