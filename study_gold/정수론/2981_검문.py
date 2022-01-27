# BOJ 2981 검문
import sys
sys.stdin = open('2981.txt')


def GCD(a, b):
    while b != 0:
        a, b = b, a%b
    return a


N = int(input())
tmp = sorted([int(input()) for _ in range(N)], reverse=True)

lst = [tmp[i-1] - tmp[i] for i in range(1, N)]
gcd = lst[0]
for i in range(1, len(lst)):
    gcd = GCD(lst[i], gcd)

res = {gcd}
for j in range(2, int(gcd**0.5)+1):
    if gcd % j == 0:
        res.add(j)
        res.add(gcd//j)
print(*sorted(list(res)))

'''
숫자 A, B, C, D를 M으로 나눴을 때 나머지가 r로 같다
A = a*M + r
B = b*M + r
C = c*M + r
D = d*M + r
빼면 
A - B = M(a-b)                                 
B - C = M(b-c)
C - D = M(c-d)
가 되므로 M이라는 최대공약수를 가진다
M의 약수들을 res에 담고 1을 제외한 값들을 출력한다
'''
