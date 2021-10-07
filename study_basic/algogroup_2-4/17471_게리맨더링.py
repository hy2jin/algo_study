# BOJ 17471 게리맨더링
import sys
from itertools import combinations
sys.stdin = open('17471.txt')


def bfs(v):
    for w in adj[v]:
        if (w in lst) and not visited[w]:
            visited[w] = 1
            bfs(w)


N = int(input())                                    # N개의 구역
population = [0] + list(map(int, input().split()))  # 1구역부터 N구역의 인구
adj = [[] for _ in range(N+1)]
for i in range(1, N+1):
    tmp = list(map(int, input().split()))
    for j in range(1, tmp[0]+1):
        adj[i] += [tmp[j]]
# print(adj)            # [[], [2, 4], [1, 3, 6, 5], [4, 2], [1, 3], [2], [2]]
'''
두 선거구 중 한곳에는 1구역이 무조건 있음
한쪽 선거구의 최대 구역 수는 N-1
'''
ans = 1e9
for i in range(1, N//2 + 1):
    A = list(combinations(range(1, N+1), i))        # 1개 구역, 2개 구역, ..., N//2개 구역
    # print(A)                          # [(1,), (2,), (3,), (4,), (5,), (6,)]
    for a in A:
        # a = list(a)                   # A선거구에 들어갈 구역의 idx --> 굳이 list로 바꿀 필요 X
        b = list(n for n in range(1, N+1) if n not in a)
        # print(a, b)                   # [1] [2, 3, 4, 5, 6]
        Va = [0] * (N+1)                # a의 visited
        Vb = [0] * (N+1)                # b의 visited

        for j in range(2):              # a와 b 각각 bfs 돌면서 visited 체크
            if j == 0:
                lst = a
                visited = Va
            else:
                lst = b
                visited = Vb
            visited[lst[0]] = 1
            bfs(lst[0])

        if sum(Va) == i and sum(Vb) == N-i:         # a와 b가 모두 인접했다면 선거구 잘 나눠진 것
            sumA = sumB = 0
            for k in range(1, N+1):
                if Va[k]:
                    sumA += population[k]
                if Vb[k]:
                    sumB += population[k]
            tmp = abs(sumA - sumB)                  # a와 b 선거구 인구수 차이
            if tmp < ans:
                ans = tmp

print(-1) if ans == 1e9 else print(ans)
