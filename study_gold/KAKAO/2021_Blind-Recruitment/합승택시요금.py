# 2021 Blind Recruitment 합승 택시 요금

n, s, a, b = 6, 4, 6, 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
# result = 82

# n, s, a, b = 7, 3, 4, 1
# fares = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
# result = 14

# n, s, a, b = 6, 4, 5, 6
# fares = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
# result = 18

'''
- 각 지점은 1 ~ n으로 표시
- s에서 출발해서 도착지는 각각 a와 b
- 지점 사이의 예상 택시 요금을 나타내는 fares
- 만약 합승하지 않고 각자 이동하는 경우가 더 저렴하면 합승하지 않아도 된다 -> default로 삼자!

- 양방향
- 3 <= n <= 200 인 자연수
- 1 <= s, a, b <= n 인 자연수이고 모두 다른 값이다
'''
from heapq import heappush, heappop
def solution(n, s, a, b, fares):
    INF = 0
    adj = [[] for _ in range(n+1)]
    for c, d, f in fares:
        adj[c].append([d, f])
        adj[d].append([c, f])
        INF += f

    def fee(i, j):                          # i에서 j로 가는 최소 요금 계산
        Q = []
        visited = [INF] * (n+1)
        heappush(Q, [0, i])
        visited[i] = 0
        while Q:
            p, v = heappop(Q)
            if p > INF: continue
            if visited[v] < p: continue
            for w, wp in adj[v]:
                np = p + wp
                if visited[w] > np:
                    visited[w] = np
                    heappush(Q, [np, w])
        return visited[j]
    sa = fee(s, a)
    sb = fee(s, b)
    ab = fee(a, b)
    ba = fee(b, a)
    answer = min(sa+sb, sa+ab, sb+ba)
    INF = answer
    for i in range(n+1):                    # s->i + i->a + i->b
        if i in [s, a, b]: continue
        tmp = fee(s, i)
        if tmp >= answer: continue
        tmp += fee(i, a)
        if tmp >= answer: continue
        tmp += fee(i, b)
        if tmp < answer:
            answer = tmp
            INF = answer

    return answer

print(solution(n, s, a, b, fares))