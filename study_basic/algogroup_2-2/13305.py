# BOJ 13305 주유소

N = int(input())                        # 도시의 개수
E = list(map(int, input().split()))     # 도로의 길이 (N-1)개
V = list(map(int, input().split()))     # 기름가격 N개

cost = V[0]
ans = V[0] * E[0]
for i in range(1, N-1):
    cost = min(cost, V[i])
    ans += cost * E[i]
print(ans)