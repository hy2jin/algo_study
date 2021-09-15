# # 2885_곱셈
# def mul(a, b):
#     tmp = []
#     for i in b[::-1]:
#         print(int(a) * int(i))
#     return int(a) * int(b)
# a = input()
# b = input()
# print(mul(a, b))

# # 2884_알람 시계
# def alarm(h, m):
#     if m < 45:
#         h -= 1
#         m += 15
#         if h == -1:
#             h = 23
#     else:
#         m -= 45
#     print(h, m)
# h, m = map(int, input().split())
# alarm(h, m)

# # 14681_사분면 고르기
# def quadrant(x, y):
#     if x > 0:
#         if y > 0:
#             return 1
#         else:
#             return 4
#     else:
#         if y > 0:
#             return 2
#         else:
#             return 3
# a = int(input())
# b = int(input())
# print(quadrant(a, b))

# # 1330_ 두 수 비교하기
# def compare(a, b):
#     if a > b:
#         return '>'
#     elif a < b:
#         return '<'
#     else:
#         return '=='
# a, b = map(int, input().split())
# print(compare(a, b))

# # 2739_구구단
# def gugudan(n):
#     for i in range(1, 10):
#         print(f'{n} * {i} = {n*i}')
# n = int(input())
# gugudan(n)

# # 10871_X보다 작은 수
# def less_num(x, seq):
#     tmp = ''
#     for i in seq:
#         if int(i) < x:
#             tmp += i + ' '
#     return tmp[:-1]
# n, x = map(int, input().split())
# seq = input().split()
# print(less_num(x, seq))

# # 1110_더하기 사이클
# def plus_cycle(n):
#     cnt = 0
#     ori_n = n
#     while True:
#         n = 10 * (n%10) + (n//10 + n%10)%10
#         cnt += 1
#         if ori_n == n:
#             break
#     return cnt
# n = int(input())
# print(plus_cycle(n))

# # 10818_최소, 최대
# def min_max(x):
#     print(min(x), max(x))
# a = input()
# b = tuple(map(int, input().split()))
# min_max(b)

# # 2562_최댓값
# def maxi(numbers):
#     print(max(numbers))
#     print(numbers.index(max(numbers)) + 1)
# tmp = []
# for _ in range(9):
#     tmp.append(int(input()))
# maxi(tmp)

# # 8958_OX퀴즈
# def OX(res):
#     cnt = 0
#     scores = []
#     for i in res:
#         if i == 'O':
#             cnt += 1
#             scores.append(cnt)
#         else:
#             cnt = 0
#     return sum(scores)
# a = int(input())
# result = []
# for _ in range(a):
#     res = input()
#     print(OX(res))

# # 2908_상수
# a, b = input().split()
# a = int(a[::-1])
# b = int(b[::-1])
# if a > b:
#     print(a)
# else:
#     print(b)

# # 4153_직각삼각형
# while True:
#     nums = list(map(int, input().split()))
#     a = nums.pop(nums.index(min(nums)))
#     c = nums.pop(nums.index(max(nums)))
#     b = nums[0]
#     if not (a or b or c):
#         break
#     if a*a + b*b == c*c:
#         print('right')
#     else:
#         print('wrong')

# # 4344_평균은 넘겠지
# C = int(input())
# for _ in range(C):
#     tc = list(map(int, input().split()))
#     N = tc.pop(0)
#     mean = sum(tc) / len(tc)
#     up = len([i for i in tc if i > mean])    # 평균 넘는 사람 수
#     per = 100 * up / len(tc)
#     print(f'{per:.3f}%')

# # 10809_알파벳 찾기
# S = input()
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# tmp = [str(S.find(c)) for c in alphabet]
# print(' '.join(tmp))

# # 1978_소수찾기
# def isprime(n):
#     if n == 1:
#         return 0
#     cnt = 0
#     for i in range(1, n+1):
#         if not (n % i):
#             cnt += 1
#             if cnt > 2: return 0
#     return 1
# N = int(input())
# numbers = list(map(int, input().split()))
# cnt = 0
# for i in numbers:
#     if isprime(i):
#         cnt += 1
# print(cnt)

# # 10250_ACM호텔
# T = int(input())
# for _ in range(T):
#     h, w, n = map(int, input().split())
#     Y, X = n % h, n // h
#     # Y == 0 (꼭대기층)
#     if not Y: print(100 * h + X)
#     else: print(100 * Y + X + 1)

# # 1712_손익분기점
# A, B, C = map(int, input().split())
# if C <= B: print(-1)
# else: print(A // (C-B) + 1)

# # 4673_셀프 넘버
# def d(num):
#     for i in str(num):
#         num += int(i)
#     return num
# self_num = [i for i in range(1, 10001)]
# for j in range(1, 9974):
#     try: self_num.remove(d(j))
#     except: pass
# for num in self_num:
#     print(num)