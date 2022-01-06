# BOJ 1929 소수 구하기

# M 이상 N 이하의 소수 모두 출력하기
M, N = map(int, input().split())

# # 2부터 N까지 숫자 중 소수가 아닌거 빼기 -> 소수만 남기기
# prime = set(range(2, N+1))
# for i in range(2, N+1):
#     # i가 소수이면 i의 배수는 소수가 아니다
#     if i in prime:
#         prime -= set(range(i*2, N+1, i))
#
# # M 이상의 소수를 출력하니까 M-1까지의 숫자는 제외하고  오름차순 출력
# prime -= set(range(M))
# prime = sorted(list(prime))
# for n in prime:
#     print(n)


# 이게 시간이 더 효율적이네
def is_prime(n):
    prime = [1] * (n+1)
    prime[0] = prime[1] = 0
    m = int(n**0.5)
    for i in range(2, m+1):
        if prime[i]:
            for j in range(i*2, n+1, i):
                prime[j] = 0
    return list(k for k in range(M, n+1) if prime[k])


prime = is_prime(N)
for num in prime:
    print(num)
