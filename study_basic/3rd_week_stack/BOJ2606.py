# BOJ 2606 바이러스


def dfs(v):
    visited[v] = 1
    for w in adj_lst[v]:
        if not visited[w]:
            dfs(w)


V = int(input())
E = int(input())
adj_lst = [[] for _ in range(V+1)]
for _ in range(E):
    n1, n2 = map(int, input().split())
    adj_lst[n1].append(n2)
    adj_lst[n2].append(n1)
visited = [0]*(V+1)
dfs(1)
print(sum(visited)-1)