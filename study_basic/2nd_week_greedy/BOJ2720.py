# BOJ2720_세탁소 사장 동혁
tc = int(input())
for _ in range(tc):
    C = int(input())
    Q, C = divmod(C, 25)
    D, C = divmod(C, 10)
    N, P = divmod(C, 5)
    print(Q, D, N, P)