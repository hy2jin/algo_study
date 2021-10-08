# BOJ 1697 숨바꼭질
from collections import deque

N, K = map(int, input().split())
if K <= N:
    print(N-K)
    exit()


def q_append(preidx, idx):
    if 0 <= idx < 200001 and visited[idx] == -1:
        visited[idx] = visited[preidx] + 1      # 걸린 시간을 나타내기 위해 직전 값 +1
        q.append(idx)
        return 1


def check(idx):
    if idx == K:
        print(visited[K])
        return 1


visited = [-1] * 200001         # visited[N]값은 N에 도달하는데 걸린 시간
q = deque()
q.append(N)
visited[N] = 0

while q:
    X = q.popleft()
    if q_append(X, X-1):
        if check(X-1): break
    if q_append(X, X+1):
        if check(X+1): break
    if q_append(X, X*2):
        if check(X*2): break
