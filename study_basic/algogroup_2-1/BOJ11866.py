# BOJ 11866 요세푸스 문제 0
N, K = map(int, input().split())
circle = list(range(1, N+1))
i = 0
ans = []
while circle:
    i = (i+K-1) % len(circle)
    ans.append(circle.pop(i))
print('<' + ', '.join(map(str, ans)) + '>')