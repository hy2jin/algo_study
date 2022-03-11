# BOJ 2658 직각이등변삼각형찾기
import sys
sys.stdin = open('2658.txt')

data = ['00000000000']
sr = er = 0
for i in range(10):
    data.append('0' + input())
    if not sr and '1' in data[i]:
        sr = i
    elif sr and '1' in data[i]:
        er = i

# 한쪽이 수직인 이등변삼각형인지 확인
if data[sr].count('1') + data[er].count('1') == 2:
    pass
# 한쪽이 수평인 이등변삼각형인지 확인
else:
    pass