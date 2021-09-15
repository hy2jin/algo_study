# BOJ 15828 Router
N = int(input())
info = []
while True:
    tmp = int(input())
    if tmp == -1:
        break
    info.append(tmp)
R = []
for i in info:
    if i == 0 and R: R.pop(0)
    elif i > 0:
        if len(R) < N: R.append(i)

print(' '.join(map(str, R))) if R else print('empty')