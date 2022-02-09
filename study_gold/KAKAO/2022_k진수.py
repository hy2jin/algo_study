# 2022 kakao blind recruitment k진수에서 소수 개수 구하기

def is_prime(n):                        # 소수인가?
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0

    trans = ''                          # k진수로 바꾸기
    while n > 0:
        n, m = divmod(n, k)
        trans = str(m) + trans
    # print(trans)

    nums = trans.split('0')             # 0으로 자르기
    # print(nums)

    for num in nums:                    # 1이랑 빈문자열 제외하기
        if num == '1' or num == '':
            continue
        if is_prime(int(num)):          # 소수이면 +1
            answer += 1
    return answer

# a = solution(437674, 3)
a = solution(110011, 10)
print(a)
