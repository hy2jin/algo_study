# BOJ 2810 컵홀더
N = int(input())
seat = input()
holder, n = 0, 0
while n < N:
    if seat[n] == 'S':
        holder += 1
        n += 1
    elif seat[n] == 'L':
        holder += 1
        n += 2
holder += 1
print(min(holder, N))