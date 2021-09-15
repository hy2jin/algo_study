# BOJ 1439 뒤집기
s = list(map(int, input()))
cnt = [0, 0]
change = s[0]
cnt[change] += 1
for i in range(1, len(s)):
    if change != s[i]:
        change = s[i]
        cnt[change] += 1
print(min(cnt))
