# BOJ 1717 집합의 표현
import sys
sys.stdin = open('1717.txt')


def find(n):                    # 루트 찾기
    if parent[n] == n:
        return n
    parent[n] = find(parent[n])
    return parent[n]


n, m = map(int, input().split())
parent = list(range(n+1))
for _ in range(m):
    tmp, a, b = map(int, input().split())
    if tmp:                     # find
        print('YES') if find(a) == find(b) else print('NO')
    else:                       # union
        p1 = find(a)
        p2 = find(b)
        if p1 != p2:            # 루트가 다르면 b의 루트를 a의 루트로
            parent[p2] = p1
