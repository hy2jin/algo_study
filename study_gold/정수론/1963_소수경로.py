# BOJ 1963 소수 경로
import sys
from collections import deque
sys.stdin = open('1963.txt')


def makeInt(lst):
    return int(''.join(lst))


def bfs(a, b):
    chk = [-1] * 10000
    chk[makeInt(a)] = 0
    Q = deque([a])
    while Q:
        lst = Q.popleft()
        if lst == b:
            return chk[makeInt(lst)]
        for i in '1234567890':
            for j in range(4):
                new = lst[:]
                new[j] = i
                new_num = makeInt(new)
                if chk[new_num] == -1 and new_num >= 1000 and is_prime[new_num]:
                    chk[new_num] = chk[makeInt(lst)] + 1
                    Q.append(new)


is_prime = [1] * 10000
is_prime[0] = is_prime[1] = 0
for i in range(2, 101):
    if is_prime[i]:
        for j in range(i+i, 10000, i):
            is_prime[j] = 0

for _ in range(int(input())):
    a, b = map(list, input().split())
    if a == b:
        print(0)
        continue
    print(bfs(a, b))
