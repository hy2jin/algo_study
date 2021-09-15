# BOJ10162 전자레인지
T = int(input())
A, T = divmod(T, 300)
B, T = divmod(T, 60)
C, T = divmod(T, 10)
print(A, B, C) if not T else print(-1)