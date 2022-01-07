# BOJ 11653 소인수분해

N = int(input())

# i = 2
# while N > 1:            # N == 1이면 그만
#     if N % i == 0:      # 나눠떨어지면
#         print(i)        # 출력
#         N //= i         # N 갱신
#     else:               # 나눠떨어지지 않으면
#         i += 1          # 다음 수


i = 2
while i*i <= N:         #
    while N % i == 0:
        print(i)
        N //= i
    i += 1
if N > 1:               # 마지막 남은 N이 소수인 경우
    print(N)
