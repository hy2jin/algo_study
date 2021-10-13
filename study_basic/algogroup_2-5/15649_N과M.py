# BOJ 15649 N과 M(1)


def perm(cnt):
    if cnt == M:
        print(*P)
        return
    for i in range(N):
        if not u[i]:
            u[i] = 1
            P[cnt] = lst[i]
            perm(cnt+1)
            u[i] = 0


N, M = map(int, input().split())
lst = list(range(1, N+1))
u = [0] * N
P = [0] * M
perm(0)
