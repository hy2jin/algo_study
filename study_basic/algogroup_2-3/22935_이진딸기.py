# BOJ 22935 이진 딸기
import sys
sys.stdin = open('22935.txt')

T = int(input())
for _ in range(T):
    N = int(input())
    n = N % 28      # 1~28 = 29~56 = 57~84
    if n > 15:
        n = 30 - n
    elif n == 0:
        n = 2
    b = bin(n)[2:]
    if len(b) < 4:
        b = '0'*(4-len(b)) + b
    ans = b.replace('0', 'V')
    ans = ans.replace('1', '딸기')
    print(ans)
