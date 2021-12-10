# BOJ 16928 뱀과 사다리 게임
import sys
from collections import deque
sys.stdin = open('16928.txt')
# input = sys.stdin.readline


def BFS():
    Q = deque([1])                      # 1번 칸에서 시작
    visited = [-1] * 101
    visited[1] = 0                      # 0번만에 도착한 칸
    while Q:
        v = Q.popleft()
        if v == 100:                    # 100번째 칸에 도착하면
            return visited[100]         # 몇번만에 도착했는지 return

        for n in range(1, 7):           # 주사위는 1부터 6까지
            nv = n + v                  # 다음 칸 숫자
            if nv > 100:                # 100을 넘어가면 소용X
                break                   # 뒷 숫자는 더 볼필요 없으니까 break
            if go[nv]:                  # 사다리나 뱀이면 이동 후의 숫자로 변경
                nv = go[nv]

            if visited[nv] == -1:
                visited[nv] = visited[v] + 1
                Q.append(nv)


N, M = map(int, input().split())        # 사다리 수 N개, 뱀의 수 M마리
go = [0] * 101
for _ in range(N+M):
    n1, n2 = map(int, input().split())
    go[n1] = n2                         # n1에 도착하면 n2로 이동시키기
print(BFS())