# BOJ 1461 도서관
import sys
sys.stdin = open('input.txt')


def cnt(lst):
    global ans
    for l in lst:
        ans += l[0] * 2
    return lst[0][0]


N, M = map(int, input().split())
left, right = [], []
tmp = list(map(int, input().split()))
for t in tmp:
    if t > 0:
        right.append(t)
    else:
        left.append(-t)
left.sort(reverse=True)
right.sort(reverse=True)
left = [left[i:i+M] for i in range(0, len(left), M)]
right = [right[j:j+M] for j in range(0, len(right), M)]
ans = 0
maxL, maxR = 0, 0
if left:
    maxL = cnt(left)
if right:
    maxR = cnt(right)
ans = ans - max(maxL, maxR)
print(ans)




