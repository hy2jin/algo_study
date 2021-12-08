# BOJ 1068 트리 (dfs)
import sys
sys.stdin = open('1068.txt')


def dfs(v):
    global cnt
    if not adj[v]:
        cnt += 1
        return
    for w in adj[v]:
        dfs(w)


def remove(v):
    while adj[v]:
        w = adj[v].pop()
        remove(w)


N = int(input())
pa = list(map(int, input().split()))
d = int(input())
adj = [[] for _ in range(N)]
for i, p in enumerate(pa):
    if p == -1:
        s = i
    else:
        adj[p].append(i)
    if i == d:
        del_p = p

if s == d:
    print(0)
    exit()

# print('before_adj :', adj)
remove(d)
adj[del_p].remove(d)
# print('after_adj :', adj)

cnt = 0
dfs(s)
print(cnt)