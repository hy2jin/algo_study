# BOJ 1065 한수

N = int(input())
if N < 100:
    print(N)
    exit()

cnt = 99
for n in range(100, N+1):
    tmp = list(map(int, str(n)))
    diff = tmp[0] - tmp[1]
    for i in range(1, len(tmp)-1):
        if diff != tmp[i] - tmp[i+1]:
            break
    else:
        cnt += 1
print(cnt)