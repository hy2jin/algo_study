# BOJ 4949 균형잡힌 세상
import sys
sys.stdin = open('input.txt')
dic = {'(': ')', '[': ']'}
while True:
    string = input()
    if string == '.':
        break
    stack = []
    ans = 'no'
    for s in string:
        if s == '(' or s == '[':
            stack.append(s)
        if s == ')' or s == ']':
            if not stack:
                break
            p = stack.pop()
            if s != dic[p]:
                break
    else:
        if not stack:
            ans = 'yes'
    print(ans)
