# BOJ 1043 거짓말
import sys
sys.stdin = open('1043.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
real = list(map(int, input().split()))[1:]          # 진실을 아는 사람들
party = [list(map(int, input().split()))[1:] for _ in range(M)]
true_party = [0] * M                # 진실을 들은 파티: 1

while real:
    t = real.pop()
    for i in range(M):
        if not true_party[i] and t in party[i]:     # 아직 진실을 들은 파티가 아니고, 진실을 아는 사람이 파티에 있으면
            true_party[i] = 1       # 진실을 들은 파티가 된다 (for문 돌면서 다시 확인할 필요 없음, 어차피 이미 진실을 아는 파티임)
            real += party[i]        # 진실을 아는 사람들에 지금 이 파티를 추가한다
            real = list(set(real))  # 공통되는 사람 제거

print(true_party.count(0))          # 거짓말을 해도 되는 파티는 아직 0인 파티
