# BOJ 3671 산업 스파이의 편지
import sys
sys.stdin = open('3671.txt')


def recur(n):
    real = int(n)
    if real > 1 and real not in cnt:        # 1은 소수가 아니니 제외, 011과 11은 같은 수니 제외
        for j in range(2, int(real**0.5)+1):
            if real % j == 0: break
        else: cnt.add(real)

    for k in range(len(nums)):              # 순열
        if not u[k]:
            u[k] = 1
            recur(n+nums[k])
            u[k] = 0


for _ in range(int(input())):
    cnt = set()
    nums = sys.stdin.readline().rstrip()
    u = [0] * len(nums)                     # 순열은 사용했는지만 체크
    for i in range(len(nums)):              # 순서가 다르면 다른 숫자로 취급
        u[i] = 1
        recur(nums[i])
        u[i] = 0
    print(len(cnt))
