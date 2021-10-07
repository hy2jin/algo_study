# BOJ 1213 팰린드롬 만들기

# string = input()
string = 'AABBBCC'
dic = {}
for s in string:
    try: dic[s] += 1
    except: dic[s] = 1
arr = sorted(dic.items(), key=lambda x:x[0], reverse=True)

odd = 0
for i in range(len(arr)):
    arr[i] = list(arr[i])
    tmp = arr[i]    # ['C', 2]
    if tmp[1] % 2:  # 알파벳이 홀수개면
        odd += 1
        odd_w = tmp[0]
# print(arr)        # [['C', 2], ['B', 3], ['A', 2]]
# print(odd_w)      # B

if odd > 1:         # 홀수개인 알파벳이 2개 이상이면 팰린드롬 X
    print("I'm Sorry Hansoo")
else:
    ans = ''
    if odd:
        ans += odd_w

    for j in range(len(arr)):
        w, n = arr[j]
        ans = w*(n//2) + ans + w*(n//2)
    print(ans)
