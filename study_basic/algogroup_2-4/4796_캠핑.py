# BOJ 4796 캠핑

tc = 1
while True:
    L, P, V = map(int, input().split())
    if L == P == V == 0:
        break
    n, r = divmod(V, P)
    ans = L*n + min(r, L)
    print(f'Case {tc}: {ans}')
    tc += 1
