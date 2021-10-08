# BOJ 2467 용액
import sys
sys.stdin = open('2467.txt')
'''
시간제한 1초
N 최대 10만, N^2: 100억 -> 1초 불가능 (이중 for X)
'''

N = int(input())
lst = list(map(int, input().split()))

# 모두 양수이거나 모두 음수인 경우
if lst[0] >= 0:
    print(lst[0], lst[1])
    exit()
if lst[N-1] <= 0:
    print(lst[N-2], lst[N-1])
    exit()


# 음수와 양수가 다 있는 경우
l, r = 0, N-1
Sum = abs(lst[l] + lst[r])
ans = [lst[l], lst[r]]
while Sum != 0:         # 0이면 그만 봐도 됨
    tmpSum = lst[l] + lst[r]
    if abs(tmpSum) < Sum:
        Sum = abs(tmpSum)
        ans = [lst[l], lst[r]]

    if l+1 == r:        # N개 숫자 다 봄
        break

    # l을 움직일지 r을 움직일지 결정
    elif tmpSum < 0:    # 음수면 같은 l에서 r이 왼쪽으로 갈수록 절대값이 커짐
        l += 1          # 다음 l로 넘어가기

    else:               # 양수면 같은 r에서 l이 오른쪽으로 갈수록 절대값이 커짐
        r -= 1          # 다음 r로 넘어가기

print(*ans)
