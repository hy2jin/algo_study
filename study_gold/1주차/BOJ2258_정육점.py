# BOJ 2258 정육점
import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
meat = [list(map(int, input().split())) for _ in range(N)]

# for i in range(N-1):
#     w, p = map(int, input().split())
#     for j in range(i+1):
#         if (p == meat[j][1] and w < meat[j][0]) or p < meat[j][1]:
#             meat.insert(j, (w, p))
#             break
#     else:
#         meat.append((w, p))

meat = sorted(meat, key=lambda x:(x[1], -x[0]))
ans = 2147483648
pre_p = meat[0][1]
for i in range(N):
    if i:
        meat[i][0] = meat[i][0] + meat[i-1][0]
        if meat[i][1] == pre_p:
            meat[i][1] += meat[i-1][1]
        else:
            pre_p = meat[i][1]
    if meat[i][0] >= M and meat[i][1] < ans:
        ans = meat[i][1]

print(ans) if ans != 2147483648 else print(-1)
