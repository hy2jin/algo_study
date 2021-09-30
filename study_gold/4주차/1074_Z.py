# BOJ 1074 Z
import sys
sys.stdin = open('1074.txt')


def recur(sr, sc, N, v):    # 시작행, 시작열, 자를수있는 횟수, 시작위치 값
    global ans
    if N == 0:              # 한칸일때
        ans = v
        return

    # R, C가 현재 행렬을 4등분 했을때 어디에 있는지 확인하고 해당되는 위치에서만 재귀
    mid = 2**(N-1)          # 현재 행렬 크기 2**N, 그 반이 중간경계
    if R < sr + mid:
        if C < sc + mid:    # 2사분면
            recur(sr, sc, N-1, v)
        else:               # 1사분면
            recur(sr, sc+mid, N-1, v+mid**2)
    else:
        if C < sc + mid:    # 3사분면
            recur(sr+mid, sc, N-1, v+2*(mid**2))
        else:               # 4사분면
            recur(sr+mid, sc+mid, N-1, v+3*(mid**2))


N, R, C = map(int, input().split())     # 3 7 7
ans = 0
recur(0, 0, N, 0)
print(ans)
