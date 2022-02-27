# 2021 Dev-Matching: 웹 백엔드 개발자 (행렬 테두리 회전하기)

rows, columns = 6, 6
queries = 	[[2,2,5,4],[3,3,6,6],[5,1,6,3]]
# result = [8, 10, 25]

# rows, columns = 3, 3
# queries = 	[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
# result = [1, 1, 5, 3]

# rows, columns = 100, 97
# queries = 	[[1,1,100,97]]
# result = [1]


def solution(rows, columns, queries):
    arr = []                            # 기본 행렬 만들기
    for row in range(rows):
        arr.append(list((row * columns) + 1 + i for i in range(columns)))

    answer = []
    for query in queries:
        x1, y1, x2, y2 = map(lambda x: x-1, query)
        nums = []
        # 위
        nums += arr[x1][y1:y2+1]
        # 오른쪽
        for r in range(x1+1, x2):  nums += [arr[r][y2]]
        # 아래
        nums += arr[x2][y1:y2+1][::-1]
        # 왼쪽
        for r in range(x2-1, x1, -1): nums += [arr[r][y1]]

        # 최소값
        answer.append(min(nums))

        # 왼쪽
        for r in range(x1, x2+1): arr[r][y1] = nums.pop()
        # 아래
        for c in range(y1+1, y2): arr[x2][c] = nums.pop()
        # 오른쪽
        for r in range(x2, x1-1, -1): arr[r][y2] = nums.pop()
        # 위
        for c in range(y2-1, y1, -1): arr[x1][c] = nums.pop()

    return answer

print(solution(rows, columns, queries))