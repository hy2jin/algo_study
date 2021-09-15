# BOJ 2839 설탕 배달
N = int(input())
cnt = 0
while True:
    if N % 5 == 0:
        cnt += N // 5
        break
    N -= 3
    cnt += 1
    if N < 0:
        cnt = -1
        break
print(cnt)