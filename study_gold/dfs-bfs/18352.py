# BOJ 18352 특정 거리의 도시 찾기 (bfs)
import sys
sys.stdin = open('18352.txt')

N, M, K, X = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)

visited = [-1] * (N+1)
q = [X]
visited[X] = 0
ans = []
while q:
    v = q.pop(0)
    for w in adj[v]:
        if visited[w] == -1:
            visited[w] = visited[v] + 1
            # 거리가 K가 되면 그 뒤는 보지 않아도 되니까 q에 안넣고
            # 출력해야하니까 ans에 넣는다
            if visited[w] == K:
                ans.append(w)
            else:
                q.append(w)

if ans:
    ans.sort()
    print('\n'.join(map(str, ans)))
else:
    print(-1)