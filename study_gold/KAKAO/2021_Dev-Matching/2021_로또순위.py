# 2021 Dev-Matching: 웹 백엔드 개발자 (로또의 최고 순위와 최저 순위)

# lottos = [44, 1, 0, 0, 31, 25]
# win_nums = [31, 10, 45, 1, 6, 19]

# lottos = [0, 0, 0, 0, 0, 0]
# win_nums = [38, 19, 20, 40, 15, 25]

lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]


def solution(lottos, win_nums):
    rank = {6: 1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    zero = lottos.count(0)
    cnt = 0
    for lot in lottos:
        for win in win_nums:
            if lot and lot == win:
                cnt += 1
                break
    return [rank[cnt+zero], rank[cnt]]

print(solution(lottos, win_nums))