# BOJ 1182 부분수열의 합
import sys
sys.stdin = open('1182.txt')


def subsum(S, idx):
    global ans
    if idx == N:
        if S == targetS:
            ans += 1
        return

    subsum(S+lst[idx], idx+1)
    subsum(S, idx+1)


N, targetS = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0
subsum(0, 0)
# targetS가 0인 경우 공집합을 제외하기 위해 -1
print(ans) if targetS else print(ans-1)
