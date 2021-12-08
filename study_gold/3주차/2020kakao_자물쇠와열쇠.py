def solution(key, lock):
    M, N = len(key), len(lock)
    # 90, 180, 270 도 회전하는 부분
    # 홈과 돌기가 맞는지 확인하는 부분
    answer = False
    return answer


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))