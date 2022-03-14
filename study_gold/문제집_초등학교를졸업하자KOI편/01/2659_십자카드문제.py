# BOJ 2659 십자키드 문제

def clock(num):
    n1 = int(num)
    n2 = int(num[1] + num[2] + num[3] + num[0])
    n3 = int(num[2] + num[3] + num[0] + num[1])
    n4 = int(num[3] + num[0] + num[1] + num[2])
    return min(n1, n2 , n3, n4)

N = ''.join(input().split())
clock_n = clock(N)

cnt = 0
for n in range(1111, 9999+1):
    if '0' in str(n):
        continue
    if clock(str(n)) == n:
        cnt += 1
    if n == clock_n:
        break

print(cnt)