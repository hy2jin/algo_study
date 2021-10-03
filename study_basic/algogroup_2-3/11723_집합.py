# BOJ 11723 집합
import sys
sys.stdin = open('11723.txt')
read = sys.stdin.readline
M = int(read()).rstrip()
S = [0]*21
for _ in range(M):
    inp = read().rstrip()

    if inp[-1].isdigit():
        w, n = inp.split()
        n = int(n)

        if w[0] == 'a':     # add
            S[n] = 1

        elif w[0] == 'c':   # check
            print(1) if S[n] else print(0)

        elif w[0] == 'r':   # remove
            S[n] = 0

        else:               # toggle
            if S[n]: S[n] = 0
            else: S[n] = 1

    else:
        if inp[0] == 'a':   # all
            S = [1]*21

        else:               # empty
            S = [0]*21
