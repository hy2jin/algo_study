# BOJ 20500 Ezreal 여눈부터 가네 ㅈㅈ
'''
15의 배수: 3의 배수이면서 5의 배수인것
1과 5로 이루어진 정수 중 15의 배수 -> 1의 자리 숫자는 무조건 5

그냥 재귀로 풀었더니 N = 1515일 때 끝나지 않는 문제가 발생함....
이렇게 오래걸리면... dp구나 싶어서 그 코드로 7까지 구하고 규칙찾음

N -> sol
1 -> 0
2 -> 1
3 -> 1
4 -> 3
5 -> 5
6 -> 11
7 -> 21
dp[n] = dp[n-1] + 2*dp[n-2]
'''


N = int(input())
dp = [0] * 1516
dp[2] = 1
for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]*2
print(dp[N] % 1000000007)
