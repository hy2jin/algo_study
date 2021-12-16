# BOJ 10971 외판원 순회 2
'''
외판원 순회 문제는 영어로 Traveling Salesman problem (TSP) 라고 불리는 문제로
computer science 분야에서 가장 중요하게 취급되는 문제 중 하나이다.
여러 가지 변종 문제가 있으나, 여기서는 가장 일반적인 형태의 문제를 살펴보자.
'''
import sys
sys.stdin = open('10974.txt')


def recur(i,  S):               # i: 현재 도시 idx, S: 현재까지의 비용
    if sum(visited) == N:       # 모든곳을 방문했으면
        global ans, si
        if arr[i][si]:          # 시작점으로 가는 길이 있으면
            ans = min(ans, S + arr[i][si])
        return
    if S >= ans:                # 방문 덜했는데 이미 비용 초과이면
        return

    for j in range(N):          # 방문하지 않았고 길이 있는 도시로 이동
        if not visited[j] and arr[i][j]:
            visited[j] = 1
            recur(j, S + arr[i][j])
            visited[j] = 0


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
ans = 1000000 * N
for si in range(N):             # 모든 도시에서 시작해보기
    visited[si] = 1
    recur(si, 0)
    visited[si] = 0
print(ans)
