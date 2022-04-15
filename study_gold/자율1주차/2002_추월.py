# BOJ 2002 추월

import sys
sys.stdin = open('2002.txt')

N = int(input())
dg = {input(): i for i in range(N)}     # 들어온 순서대로 차에 번호 (0, 1, ...)
out = [0] * N               # 나간 차의 idx는 1

cnt = 0
for _ in range(N):
    ys = input()
    j = dg[ys]              # 이 차의 번호는 j
    s = sum(out[:j])        # 앞 번호 차들 중 나간 차의 수
    if s < j: cnt += 1      # 앞 번호 차들이 덜 나갔다는건 이 차가 추월을 했다는 의미
    out[j] = 1              # 이 차가 나갔다고 표시
print(cnt)
