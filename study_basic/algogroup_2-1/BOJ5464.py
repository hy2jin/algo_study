# BOJ 5464 주차장
import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
R = [[0, 0]] + [[0, int(input())] for _ in range(N)]        # [주차된 차량번호, 주차요금]
W = [0] + [int(input()) for _ in range(M)]                  # [차량무게]
inout = [int(input()) for _ in range(2*M)]                  # 차량 들어오고 나가는 순서
Q = []          # 주차 공간 꽉 차서 기다려야하는 차량
q, ans = 0, 0
for io in inout:
    if io > 0:
        for r in range(1, N+1):
            if not R[r][0]:
                R[r][0] = io
                ans += R[r][1] * W[io]
                break
        else:
            Q.append(io)
    else:
        for r in range(1, N+1):
            if R[r][0] == -io:
                if len(Q) != q:
                    R[r][0] = Q[q]
                    ans += R[r][1] * W[Q[q]]
                    q += 1
                else:
                    R[r][0] = 0
print(ans)