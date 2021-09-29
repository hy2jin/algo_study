# BOJ 1780 종이의 개수
import sys
sys.stdin = open('1780.txt')


def check_paper(arr):
    paper_cnt = [0, 0, 0]           # 0 개수, 1 개수, -1 개수
    L = len(arr)
    BP = L*L                        # breakpoint
    for lst in arr:
        mone, zero = lst.count(-1), lst.count(0)
        one = L - mone - zero
        paper_cnt[-1] += mone
        paper_cnt[0] += zero
        paper_cnt[1] += one

    for i in range(3):              # 모두 같은 숫자로 이루어진 종이
        if paper_cnt[i] == BP:
            ans[i] += 1
            return

    if L == 3:                      # 길이가 3인데 위에서 return이 안됨 --> 다음 종이들은 모두 크기가 1
        for i in range(3):          # 그냥 그 숫자들 더해주면 재귀 안해도 됨
            ans[i] += paper_cnt[i]
        return

    for r in range(0, L, L//3):
        for c in range(0, L, L//3):
            new = []                # 재귀호출할때 들어갈 배열 생성
            for k in range(L//3):
                new.append(arr[r+k][c:c+L//3])
            check_paper(new)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = [0, 0, 0]                     # 0 개수, 1 개수, -1 개수
check_paper(arr)
print(ans[-1])
print(ans[0])
print(ans[1])
