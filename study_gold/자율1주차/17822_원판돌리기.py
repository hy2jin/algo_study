# BOJ 17822 원판 돌리기
import sys
from collections import deque
sys.stdin = open('17822.txt')

# N번째 원판까지, M개의 정수가 적혀있다
N, M, T = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(N)]

# 총 T번 회전시킨다
for _ in range(T):
    # 번호가 x의 배수인 원판을 d 방향으로 k칸 회전시킨다
    x, d, k = map(int, input().split())
    for nth in range(x-1, N, x):
        Q = deque(nums[nth])
        # d = 0이면 시계 방향, d = 1이면 반시계 방향
        Q.rotate(-k) if d else Q.rotate(k)
        nums[nth] = list(Q)

    # 나중에 0으로 만들어줄 위치
    delRC = set()

    # 전체를 돌면서 0이 아니면 인접한곳 확인
    for n in range(N):
        for m in range(M):
            if nums[n][m] == 0: continue

            # 같은 값의 위치
            tmpRC = []
            NUM = nums[n][m]

            if m == 0:
                if NUM == nums[n][1]: tmpRC.append((n, 1))
                if NUM == nums[n][M - 1]: tmpRC.append((n, M - 1))
            elif m == M-1:
                if NUM == nums[n][M - 2]: tmpRC.append((n, M - 2))
                if NUM == nums[n][0]: tmpRC.append((n, 0))
            elif 1 <= m <= M - 2:
                if NUM == nums[n][m - 1]: tmpRC.append((n, m - 1))
                if NUM == nums[n][m + 1]: tmpRC.append((n, m + 1))

            if n == 0:
                if NUM == nums[1][m]: tmpRC.append((1, m))
            elif n == N-1:
                if NUM == nums[N - 2][m]: tmpRC.append((N - 2, m))
            elif 1 <= n <= N - 2:
                if NUM == nums[n - 1][m]: tmpRC.append((n - 1, m))
                if NUM == nums[n + 1][m]: tmpRC.append((n + 1, m))

            if len(tmpRC):
                for tup in tmpRC:
                    delRC.add(tup)
                delRC.add((n, m))

    if len(delRC) == 0:
        S = cnt = 0
        for a in range(N):
            for b in range(M):
                if nums[a][b]:
                    S += nums[a][b]
                    cnt += 1
        if cnt:
            avg = S/cnt
            for a in range(N):
                for b in range(M):
                    if nums[a][b]:
                        if nums[a][b] > avg: nums[a][b] -= 1
                        elif nums[a][b] < avg: nums[a][b] += 1
        else: break

    else:
        for delR, delC in delRC:
            nums[delR][delC] = 0
        # nums[n][m] = 0

ans = 0
for lst in nums:
    ans += sum(lst)
print(nums)
print(ans)

