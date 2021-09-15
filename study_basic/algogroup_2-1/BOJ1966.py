# BOJ 1966 프린터 큐
import sys
sys.stdin = open('input.txt')


for _ in range(int(input())):
    N, idx = map(int, input().split())
    q = list(map(int, input().split()))
    q_idx = list((q[i], i) for i in range(N))
    q.sort(reverse=True)

    j = 0
    cnt = 0
    while q_idx:
        if q_idx[0][0] != q[j]:
            q_idx.append(q_idx.pop(0))
        else:
            cnt += 1
            if q_idx[0][1] == idx:
                print(cnt)
                break
            q_idx.pop(0)
            j += 1