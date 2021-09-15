# 18238_ZOAC2
word = input()
T, start = 0, 'A'
for w in word:
    diff = abs(ord(w) - ord(start))
    T += min(diff, 26-diff)
    start = w
print(T)