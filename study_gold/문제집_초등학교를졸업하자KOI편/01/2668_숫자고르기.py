# BOJ 2668 숫자고르기
import sys
sys.stdin = open('2668.txt')
input = sys.stdin.readline

def recur(idx, num, i):
    idx.add(i)
    num.add(data[i])
    if data[i] in idx:
        if idx == num:          # 한 사이클 완성
            ans.update(idx)     # ans에 추가
        return
    return recur(idx, num, data[i])

N = int(input())
data = [0] + [int(input()) for _ in range(N)]

ans = set()
for i in range(1, N+1):
    if i not in ans:            # 아직 추가된 숫자가 아니면
        recur(set(), set(), i)  # 사이클

print(len(ans))
for an in sorted(list(ans)):
    print(an)
