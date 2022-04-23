# BOJ 1713 후보 추천하기
import sys
sys.stdin = open('1713.txt')


def recommend(time, n):             # 시간, 학생번호
    frame.sort()
    for m in range(M):
        if n == frame[m][2]:        # 사진틀에 있는 학생이면
            frame[m][0] += 1        # 추천수 +1
            return

    frame.pop(0)                    # 사진틀에 없는 학생이면
    frame.append([1, time, n])      # 가장 앞 빼고 추천수 1인 현재 학생 추가


M = int(input())                                # 사진틀 수
frame = [[0, 0, 0] for _ in range(M)]           # 사진틀: [추천, 시간, 학생번호]
N = int(input())                                # 추천 횟수
students = list(map(int, input().split()))      # 추천받은 학생 번호

for i in range(N):
    recommend(i, students[i])

ans = []
for lst in frame:
    if lst[2]:                      # 추천받은 학생 수가 사진틀 수보다 작은 경우
        ans += [lst[2]]
print(*sorted(ans))
