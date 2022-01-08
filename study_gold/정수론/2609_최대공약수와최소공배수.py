# BOJ 2609 최대공약수와 최소공배수
'''
유클리드 호제법: 주어진 두 수 사이에 존재하는 최대공약수(GCD)를 구하는 알고리즘
24 18 -> 24 % 18 = 6
18 6 -> 18 % 6 = 0
6 0 -> GCD = 6
LCM = 24 * 18 / 6 = 72
'''


def GCD(a, b):
    if b > a:
        a, b = b, a
    while b != 0:
        a, b = b, a%b
    return a


a, b = map(int, input().split())
gcd = GCD(a, b)
print(gcd)
print(a * b // gcd)
