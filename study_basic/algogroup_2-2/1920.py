# BOJ 1920 수 찾기
import sys
sys.stdin = open('1920.txt')
N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
num = list(map(int, input().split()))

for n in num:
    s, e = 0, N-1
    ans = 0
    while s <= e:
        i = (s+e)//2
        tmp = A[i]
        if A[i] == n:
            ans = 1
            break
        elif A[i] > n:
            e = i-1
        else:
            s = i+1
    print(ans)