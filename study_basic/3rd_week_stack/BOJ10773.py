# BOJ 10773 제로
K = int(input())
stack = []
ans = 0
for _ in range(K):
    n = int(input())
    if n:
        ans += n
        stack.append(n)
    else:
        ans -= stack.pop()
print(ans)
