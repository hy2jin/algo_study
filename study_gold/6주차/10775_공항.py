# BOJ 10775 공항
import sys
# input = sys.stdin.readline
sys.stdin = open('10775.txt')


def find(n):
    if n != parent[n]:
        parent[n] = find(parent[n])
    return parent[n]


def union(n1, n2):
    p1 = parent[n1]
    p2 = parent[n2]
    parent[p2] = p1


G = int(input())
P = int(input())
plane = [int(input()) for _ in range(P)]
parent = list(range(G+1))
# print(f'처음 상태: {parent}')
cnt = 0
for p in plane:
    pp = find(p)
    if pp == 0:
        break
    union(pp-1, pp)
    # print(f'{p}번 비행기 -> {parent}')
    cnt += 1


print(cnt)


'''
G = int(input())
P = int(input())
gate = [0] * (G+1)
for i in range(P):
    g = int(input())
    while g > 0:
        if gate[g] == 0:
            gate[g] = 1
            break
        else:
            g -= 1
    if g == 0:
        break
print(i)
'''