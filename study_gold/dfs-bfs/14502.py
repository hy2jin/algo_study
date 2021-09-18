# BOJ 14502 연구소 (bfs)
'''
2차원 배열 slicing으로 deepcopy
'''
import sys
sys.stdin = open('14502.txt')
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def bfs(q, lab):
    two = 0
    while q:
        r, c = q.pop(0)
        for d in range(4):
            nr, nc = r+dr[d], c+dc[d]
            if 0 <= nr < N and 0 <= nc < M and not lab[nr][nc]:
                lab[nr][nc] = 2
                two += 1
                q.append((nr, nc))
    return cnt - two - 3


N, M = map(int, input().split())
arr = []
virus = []
zero = []
cnt = 0
for n in range(N):
    tmp = list(map(int, input().split()))
    for idx, t in enumerate(tmp):
        if t == 0:
            zero.append((n, idx))
            cnt += 1
        if t == 2:
            virus.append((n, idx))
    arr.append(tmp)
ans = 0
for i in range(len(zero)-2):
    for j in range(i+1, len(zero)-1):
        for k in range(j+1, len(zero)):
            lab = [tmp[:] for tmp in arr]
            ir, ic = zero[i]
            jr, jc = zero[j]
            kr, kc = zero[k]
            lab[ir][ic], lab[jr][jc], lab[kr][kc] = 1, 1, 1
            ans = max(ans, bfs([temp[:] for temp in virus], lab))
print(ans)