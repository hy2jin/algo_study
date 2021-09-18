# BOJ 1068 트리 (dfs)
import sys
sys.stdin = open('1068.txt')


def dfs(v):
    global cnt
    for w in adj[v]:
        if w != d and not visited[w]:
            visited[w] = 1
            dfs(w)
            if not adj[w]:
                cnt += 1


N = int(input())
pa = list(map(int, input().split()))
d = int(input())
# print('pa :', pa)

adj = [[] for _ in range(N)]
for i in range(N):
    if pa[i] == -1:
        s = i
    else:
        adj[pa[i]].append(i)
if s == d:
    print(0)
    exit()
# print('adj :', adj)
cnt = 0
visited = [0] * N
visited[s] = 1
# print('start point :', s)
dfs(s)
print(cnt) if cnt else print(1)