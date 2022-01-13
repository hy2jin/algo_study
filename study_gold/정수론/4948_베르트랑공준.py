# BOJ 4948 베르트랑 공준
import sys
sys.stdin = open('4948.txt')


N = 123456*2 + 1                        # 범위 숫자 미리 구해놓기
is_prime = [1] * N
is_prime[0] = is_prime[1] = 0

for i in range(2, int(N**0.5)+1):       # 범위 중요! int(N**0.5)까지 봐야하니까 +1 해준다!
    if is_prime[i]:
        for j in range(i*2, N, i):
            is_prime[j] = 0


while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    print(sum(is_prime[n+1 : 2*n+1]))
