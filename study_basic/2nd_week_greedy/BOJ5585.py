# 5585 거스름돈
pay = 1000 - int(input())
cnt = 0

coin = [500, 100, 50, 10, 5, 1]
for i in coin:
    n, pay = divmod(pay, i)
    cnt += n
print(cnt)