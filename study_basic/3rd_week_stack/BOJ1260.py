# BOJ 1260 DFS와 BFS

def DFS(v):
    visited_D[v] = 1
    dfs.append(v)
    for w in range(1, V+1):
        if not visited_D[w] and adj_arr[v][w]:
            DFS(w)


def BFS(v):
    q = [v]
    visited_B[v] = 1
    while q:
        now = q.pop(0)
        bfs.append(now)
        for w in range(1, V+1):
            if not visited_B[w] and adj_arr[now][w]:
                q.append(w)
                visited_B[w] = 1


V, E, sp = map(int, input().split())
adj_arr = [[0] * (V+1) for _ in range(V+1)]
dfs, bfs = [], []
visited_D, visited_B = [0] * (V+1), [0] * (V+1)
for _ in range(E):
    n1, n2 = map(int, input().split())
    adj_arr[n1][n2] = 1
    adj_arr[n2][n1] = 1
DFS(sp)
BFS(sp)
print(' '.join(map(str, dfs)) + '\n' + ' '.join(map(str, bfs)))
