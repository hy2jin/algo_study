# BOJ 1978 소수 찾기
import sys
sys.stdin = open('1978.txt')
'''
소수: 1과 자신 이외의 자연수로는 나눠떨어지지 않는 1보다 큰 자연수
'''


def isprime(n):
    # 0과 1은 소수가 아님
    if n < 2:
        return 0

    cnt = 0
    for i in range(1, n+1):
        if (n % i) == 0:
            cnt += 1
            # 소수는 1과 자기자신으로만 나눠떨어지니까 cnt == 2 이다, 2보다 커지면 소수가 아님
            if cnt > 2:
                return 0
    return 1


N = int(input())
nums = list(map(int, input().split()))
ans = 0
for num in nums:
    # 소수인가?
    if isprime(num):
        ans += 1
print(ans)
