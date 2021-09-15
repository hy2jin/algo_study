# BOJ 19539 사과나무
import sys
sys.stdin = open('input.txt')

N = int(input())
tree = tuple(map(int, input().split()))

n, i = divmod(sum(tree), 3)
if i:
    print('NO')
    exit()

two = 0
for t in tree:
    two += t//2

print('NO') if two < n else print('YES')
