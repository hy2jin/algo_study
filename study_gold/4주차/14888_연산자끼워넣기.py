# BOJ 14888 연산자 끼워넣기
import sys
from itertools import permutations
sys.stdin = open('14888.txt')

N = int(input())                            # 숫자의 개수
A = list(map(int, input().split()))         # 숫자 리스트


lst = ['+', '-', '*', '/']
count = list(map(int, input().split()))     # 몇개씩 들어있는가?
eq_tmp = []                                 # 일단 나열
for i in range(len(count)):
    n = count[i]
    eq_tmp.extend(lst[i] * n)
# print(eq_tmp)

eq = list(set(permutations(eq_tmp, N-1)))   # 기호 순열 리스트(중복 제외하기 위한 set)
# print(eq)

mans, Mans = 9876543210, -9876543210        # min ans, max ans
for e in eq:
    # print(e)
    ans = A[0]
    for i in range(N-1):
        if e[i] == '+':
            ans += A[i+1]
        elif e[i] == '-':
            ans -= A[i+1]
        elif e[i] == '*':
            ans *= A[i+1]
        else:
            ans = int(ans/A[i+1])

    if ans > Mans:
        Mans = ans
    if ans < mans:
        mans = ans

print(Mans)
print(mans)
