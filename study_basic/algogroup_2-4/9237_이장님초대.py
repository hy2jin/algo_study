# BOJ 9237 이장님 초대

N = int(input())
t = list(map(int, input().split()))
t.sort()
day = 0
for i in range(N):
    if day < t[i] - i:
        day = t[i] - i
print(day+N+1)
