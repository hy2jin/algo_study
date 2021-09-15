# BOJ 1448 삼각형 만들기
'''
* st[i] < st[i+1] + st[i+2]를 만족하지 못하면
오른쪽 항에 st의 어떤 수가 들어와도 불가능
'''
import sys
read = sys.stdin.readline
N = int(read())
st = [int(read()) for _ in range(N)]
st.sort(reverse=True)
ans = -1
for i in range(N-2):
    if st[i] < st[i+1] + st[i+2]:
        ans = st[i] + st[i+1] + st[i+2]
        break
print(ans)