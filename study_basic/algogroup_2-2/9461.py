# BOJ 9461 파도반 수열

lst = [0]*101
lst[1], lst[2], lst[3] = 1, 1, 1
for i in range(4, 101):
    lst[i] = lst[i-2] + lst[i-3]

for _ in range(int(input())):
    print(lst[int(input())])