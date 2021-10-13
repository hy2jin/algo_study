# BOJ 6603 로또
import sys
sys.stdin = open('6603.txt')


def recur(cnt, si):
    if cnt == 6:
        print(*P)
        return
    for i in range(si, k):
        P[cnt] = S[i]
        recur(cnt+1, i+1)


while True:
    inp = input()
    if inp == '0':
        break
    S = list(map(int, inp.split()))
    k = S.pop(0)
    P = [0] * 6
    recur(0, 0)
    print()
