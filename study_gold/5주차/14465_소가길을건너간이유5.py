# BOJ 14465 소가 길을 건너간 이유5
import sys
sys.stdin = open('14465.txt')

N, K, B = map(int, input().split())
light = [0] * N
for n in range(B):
    light[int(input())-1] = 1       # 고장난 신호등 1
# print(light)

pre = sum(light[:K])
ans = pre
for i in range(N-K):
    # pre에 계산된 것들 중 제일 앞에꺼 빼고 다음꺼 하나 더해주기
    pre = pre - light[i] + light[K+i]
    ans = min(pre, ans)

print(ans)
