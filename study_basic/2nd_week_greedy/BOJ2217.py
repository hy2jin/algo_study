# BOJ 2217 로프
N = int(input())
rope = [int(input()) for _ in range(N)]
rope.sort(reverse=True)

maxW = 0
for _ in range(N):
    if rope[-1] * len(rope) > maxW:
        maxW = rope[-1] * len(rope)
    rope.pop()
print(maxW)