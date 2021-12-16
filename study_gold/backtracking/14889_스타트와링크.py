# BOJ 14889 스타트와 링크
import sys
sys.stdin = open('14889.txt')
# input = sys.stdin.readline


def combi(si, cnt):
    if cnt == N//2:                     # 한 팀에 N//2명 다 뽑음
        team1 = []
        team2 = []
        for n in range(N):              # 팀 만들기
            if u[n]: team1.append(n)
            else: team2.append(n)
        if tuple(team1) not in chk:     # 확인한적 있는지 체크
            global ans
            sum1 = calc(team1)          # 능력치 계산
            sum2 = calc(team2)
            tmp = abs(sum1 - sum2)      # 차이의 절대값
            if tmp < ans:
                ans = tmp               # 갱신
            chk.add(tuple(team1))       # 확인했다고 표시
            chk.add(tuple(team2))
        return

    for j in range(si, N):              # 팀원 덜 뽑았으면 계속 뽑기
        u[j] = 1
        combi(j+1, cnt+1)
        u[j] = 0


def calc(lst):
    s = 0
    for i in range(N//2 - 1):
        for j in range(i+1, N//2):
            s += arr[lst[i]][lst[j]] + arr[lst[j]][lst[i]]
    return s


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 100 * N * N       # Sij는 최대 100
u = [0] * N             # 조합 만들고 팀원 데려갈때 쓰려고
chk = set()             # (1, 2), (3, 4) / (3, 4), (1, 2) 같은 경우를 제거하려고 체크를 위해
for i in range(N):      # 조합
    u[i] = 1
    combi(i+1, 1)
    u[i] = 0
print(ans)
