# BOJ 2251 물통

def calc(fr, to, etc):          # fr에서 to로 물을 붓는다
    to, To = to
    tmp = fr + to
    if tmp < To:                # to에 다 부을 수 있는 경우
        to = tmp
        fr = 0
    else:                       # to가 꽉차서 덜 붓는 경우
        to = To
        fr = tmp - To
    return fr, to, etc          # 물 다 붓고 return


def chk_recur(a, b, c):
    if (a, b, c) not in chk:    # 지금 물 양 이전에 거쳐갔는지 확인
        chk.append((a, b, c))   # 처음이면 추가하고
        recur((a, b, c))        # 물 부으러 ㄱㄱ


def recur(water):
    a, b, c = water             # 현재 A, B, C에 담긴 물의 양
    if a:                       # A에 물이 있다
        if b < B:               # B에 부을 수 있다
            x, y, z = calc(a, (b, B), c)
            chk_recur(x, y, z)
        if c < C:               # C에 부을 수 있다
            x, z, y = calc(a, (c, C), b)
            chk_recur(x, y, z)

    if b:                       # B에 물이 있다
        if a < A:               # A에 부을 수 있다
            y, x, z = calc(b, (a, A), c)
            chk_recur(x, y, z)
        if c < C:               # C에 부을 수 있다
            y, z, x = calc(b, (c, C), a)
            chk_recur(x, y, z)

    if c:                       # C에 물이 있다
        if b < B:               # B에 부을 수 있다
            z, y, x = calc(c, (b, B), a)
            chk_recur(x, y, z)
        if a < A:               # A에 부을 수 있다
            z, x, y = calc(c, (a, A), b)
            chk_recur(x, y, z)


# A, B, C = map(int, input().split())
A, B, C = 8, 9, 10
chk = [(0, 0, C)]
# 모든 경우를 다 보고 나서
recur((0, 0, C))
# A가 0일때 C 구하기
ans = set()
for lst in chk:
    if not lst[0]:
        ans.add(lst[2])
ans = sorted(list(ans))
print(*ans)
