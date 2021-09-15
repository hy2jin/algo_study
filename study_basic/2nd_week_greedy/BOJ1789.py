# BOJ 1789 수들의 합
S = int(input())
tmp = 0
for i in range(1, S):
    tmp += i
    if tmp > S:
        i -= 1
        break
print(i)