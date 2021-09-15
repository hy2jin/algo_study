# BOJ 18258 큐 2
import sys
sys.stdin = open('input.txt')
# read = sys.stdin.readline
N = int(input())
q = []
idx = 0
for _ in range(N):
    tmp = input()
    if tmp == 'pop':
        if len(q) - idx:
            print(q[idx])
            idx += 1
        else:
            print(-1)
    elif tmp == 'size':
        print(len(q) - idx)
    elif tmp == 'empty':
        if len(q) - idx:
            print(0)
        else:
            print(1)
    elif tmp == 'front':
        if len(q) - idx:
            print(q[idx])
        else:
            print(-1)
    elif tmp == 'back':
        if len(q) - idx:
            print(q[-1])
        else:
            print(-1)
    else:
        q += [tmp.split()[1]]
