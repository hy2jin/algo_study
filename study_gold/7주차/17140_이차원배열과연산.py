# BOJ 17140 이차원 배열과 연산
import sys
# input = sys.stdin.readline
sys.stdin = open('17140.txt')

R, C, k = map(int, input().split())
R -= 1
C -= 1
A = [list(map(int, input().split())) for _ in range(3)]


def rsort():
    maxL = 0
    for r in range(len(A)):
        check = set()
        tmp = []
        for n in A[r]:
            if not n in check:
                check.add(n)
                tmp.append([n, A[r].count(n)])
        tmp.sort(key=lambda x: (x[1], x[0]))
        Ar = []
        for lst in tmp:
            Ar.extend(lst)
        A[r] = Ar
        if maxL < len(Ar):
            maxL = len(Ar)
    for r in range(len(A)):
        if len(A[r]) < maxL:
            A[r] += [0] * (maxL - len(A[r]))


for t in range(100):
    if A[R-1][C-1] == k:
        print(t)
        break
    # R 연산
    if len(A) >= len(A[0]):
        rsort()
    # C 연산
    else:
        A = list(map(list, zip(*A)))
        rsort()
        A = list(map(list, zip(*A)))
else:
    print(-1)
