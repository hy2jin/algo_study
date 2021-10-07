# BOJ 2078 무한이진트리

a, b = map(int, input().split())
l = r = 0
while True:
    if a == 1:          # lv1 오른쪽
        r += b-1
        break
    elif b == 1:        # lv1 왼쪽
        l += a-1
        break

    if a > b:           # 왼쪽에서 내려왔음
        l += a//b       # 한번에 올라갈 lv
        a %= b          # 오른쪽 값은 그대로

    else:               # 오른쪽에서 내려왔음
        r += b//a
        b %= a

print(l, r)
