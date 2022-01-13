# BOJ 2023 신기한 소수


def is_prime(n):                    # 소수인가?
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def recur(num):
    if len(num) == N:               # num이 N자리 숫자면 출력하고 return
        print(num)
        return

    for n in '1379':
        nn = num + n
        if is_prime(int(nn)):       # nn이 소수이면 재귀
            recur(nn)


N = int(input())
for n in '2357':
    recur(n)
