# BOJ 2580 스도쿠
import sys
sys.stdin = open('2580.txt')
# input = sys.stdin.readline


def recur(depth):
    # 빈칸 다 채우면 출력하고 종료
    if depth == Depth:
        for i in range(9):
            print(*arr[i])
        exit()

    r, c = zero[depth]          # 이번에 채울 좌표
    check = set()               # 의 가로, 세로, 3x3에 존재하는 숫자들
    for j in range(9):
        check.add(arr[r][j])    # 가로 담기
        check.add(arr[j][c])    # 세로 담기
    rr = 3 * (r//3)
    cc = 3 * (c//3)
    for x in range(3):          # 3x3 담기
        for y in range(3):
            check.add(arr[rr + x][cc + y])

    # 1~9에서 존재하는거 빼면 빈칸에 넣을 수 있는 숫자들
    num_list = list(set(range(1, 10)) - check)

    for n in num_list:
        arr[r][c] = n
        recur(depth + 1)
        # num_list가 없어서 return되어 돌아온 경우 지금 좌표의 숫자를 바꿔야 함
        # 만약 지금 대입한 n이 num_list의 마지막 값이면 그대로 return 되는데 그러면 안됨
        # --> arr[r][c] 값을 0으로 바꿔줘야 함
        arr[r][c] = 0


arr = []
zero = []
for i in range(9):
    arr.append(list(map(int, input().split())))
    for j in range(9):
        if not arr[i][j]:
            zero.append((i, j))
Depth = len(zero)
recur(0)
