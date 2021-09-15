# BOJ 9012 괄호

def VPS(gualho):
    stack = []
    for g in gualho:
        if not stack or g == '(':
            stack.append(g)
        elif g == ')':
            if not stack:
                return 'NO'
            s = stack.pop()
            if s != '(':
                return 'NO'
    if stack:
        return 'NO'
    return 'YES'

T = int(input())
for _ in range(T):
    print(VPS(input()))