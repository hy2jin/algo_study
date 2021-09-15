# BOJ11399_ATM
N = int(input())
time = list(map(int, input().split()))
time.sort()
wait = []
for i in range(N):
    wait.append(sum(time[:i+1]))
print(sum(wait))