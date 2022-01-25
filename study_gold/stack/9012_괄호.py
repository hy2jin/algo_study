# BOJ 9012 괄호
import sys
sys.stdin = open('9012.txt')


def VPS(ip):
    stk = []
    for i in ip:
        if i == '(':
            stk.append(i)
        else:
            if not stk or stk[-1] == ')':
                return 'NO'
            else:
                stk.pop()
    if stk:
        return 'NO'
    return 'YES'


for _ in range(int(input())):
    print(VPS(input()))
