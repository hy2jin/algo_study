# BOJ 2012 등수 매기기

N = int(input())
arr = [int(input()) for _ in range(N)] + [0]
arr.sort()
ans = 0
for i in range(1, N+1):
    ans += abs(i-arr[i])
print(ans)
