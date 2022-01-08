# BOJ 2581 소수


def prime(n):
    nums = [1] * (n+1)
    nums[0] = nums[1] = 0
    for i in range(2, n+1):
        if nums[i]:
            for j in range(i*2, n+1, i):
                nums[j] = 0
    # M 이상 n 이하의 소수만 return
    return [k for k in range(M, n+1) if nums[k]]


M = int(input())
N = int(input())
MtoN = prime(N)

# M 이상 N 이하의 자연수 중 소수가 있는 경우
if MtoN:
    print(sum(MtoN))
    print(MtoN[0])
# 소수가 없는 경우
else:
    print(-1)
