# BOJ 2251 물통

def calc(fr, to, etc):
    to, To = to
    tmp = fr + to
    if tmp < To:
        to = tmp
        fr = 0
    else:
        to = To
        fr = tmp - To
    return fr, to, etc


def chk_recur(a, b, c):
    if (a, b, c) not in chk:
        chk.append((a, b, c))
        recur((a, b, c))


def recur(water):
    a, b, c = water
    if a:
        if b < B:
            x, y, z = calc(a, (b, B), c)
            chk_recur(x, y, z)
        if c < C:
            x, z, y = calc(a, (c, C), b)
            chk_recur(x, y, z)
    if b:
        if a < A:
            y, x, z = calc(b, (a, A), c)
            chk_recur(x, y, z)
        if c < C:
            y, z, x = calc(b, (c, C), a)
            chk_recur(x, y, z)
    if c:
        if b < B:
            z, y, x = calc(c, (b, B), a)
            chk_recur(x, y, z)
        if a < A:
            z, x, y = calc(c, (a, A), b)
            chk_recur(x, y, z)


# A, B, C = map(int, input().split())
A, B, C = 8, 9, 10
chk = [(0, 0, C)]
recur((0, 0, C))
ans = set()
for lst in chk:
    if not lst[0]:
        ans.add(lst[2])
ans = sorted(list(ans))
print(*ans)
