# BOJ 1978 소수 찾기
import sys
sys.stdin = open('1978.txt')
'''
소수: 1과 자신 이외의 자연수로는 나눠떨어지지 않는 1보다 큰 자연수
-> 에라토스테네스의 체
1. 2부터 N까지 모두 소수(True)라는 리스트를 만든다
2. 2부터 순서대로 확인하면서 소수이면 그 숫자의 배수들은 소수가 아님(False)으로 바꾼다
3. N의 최대 약수는 N**0.5니까 int(N**0.5)보다 큰 수들은 체크할 필요가 없다
   -> 이전에 더 작은 수의 배수로 체크가 되고 소수만 남아있음
    ex) n = 36이면 6까지 확인?
    2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36
    2 / 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35
    2 3 / 5 7 11 13 17 19 23 25 29 31 35
    2 3 5 / 7 11 13 17 19 23 29 31
'''


# # 오래걸림
# def isprime(n):
#     # 0과 1은 소수가 아님
#     if n < 2:
#         return 0
#     cnt = 0
#     for i in range(1, n+1):
#         if (n % i) == 0:
#             cnt += 1
#             # 소수는 1과 자기자신으로만 나눠떨어지니까 cnt == 2 이다, 2보다 커지면 소수가 아님
#             if cnt > 2:
#                 return 0
#     return 1
# N = int(input())
# nums = list(map(int, input().split()))
# ans = 0
# for num in nums:
#     # 소수인가?
#     if isprime(num):
#         ans += 1
# print(ans)



# 에라토스테네스의 체
def is_prime(n):
    prime = [1] * (n+1)
    prime[0] = prime[1] = 0
    # n의 최대 약수는 n**0.5 이하니까 2부터 n**0.5까지 체크
    m = int(n**0.5)
    for i in range(2, m+1):
        # i가 소수이면 i의 배수들은 소수가 아니니까 0으로 만들기
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = 0
    return prime


def is_prime2(n):
    prime = set(range(2, n+1))
    for i in range(2, n+1):
        if i in prime:
            prime -= set(range(2*i, n+1, i))
    return prime


N = int(input())
nums = list(map(int, input().split()))
prime = is_prime(1000)
prime2 = is_prime2(1000)
ans1 = 0
ans2 = 0
for num in nums:
    if prime[num]:
        ans1 += 1
    if num in prime2:
        ans2 += 1
print(ans1)
print(ans2)
