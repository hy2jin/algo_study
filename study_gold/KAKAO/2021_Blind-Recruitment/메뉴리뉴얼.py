# 2021 Blind Recruitment 메뉴 리뉴얼
from itertools import combinations

# orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
# course = [2,3,4]
# result = ["AC", "ACDE", "BCFG", "CDE"]

# orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
# course = [2,3,5]
# result = ["ACD", "AD", "ADE", "CD", "XYZ"]

orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
# result = ["WX", "XY"]
'''
- 코스요리 메뉴는 최소 2개 이상의 단품메뉴로 구성
- 최소 2명 이상의 손님으로부터 주문된 메뉴 조합만 후보에 포함
- 각 손님은 단품메뉴 2개이상 주문해야하며, 단품메뉴는 A ~ Z로 표기(대문자)
- return 값은 오름차순 정렬하기
'''
def solution(orders, course):
    dic = {}                                    # 코스: 몇번나옴
    length = {k: [] for k in course}            # 길이: 해당되는 코스들

    # dic 만들기
    for order in orders:
        for n in course:
            # order 정렬해서 조합 만들기!!
            for combi in combinations(sorted(order), n):
                dic[combi] = dic.get(combi, 0) + 1
    # print(dic)
    # dic = {('A', 'B'): 1, ('A', 'C'): 4, ('A', 'F'): 1, ('A', 'G'): 1, ('B', 'C'): 2 ...}

    # lenth 만들기
    for k, v in dic.items():
        if v == 1: continue                     # 2번 이상 나온게 아니면 pass
        if len(k) not in length: continue       # course에 있는 길이가 아니면 pass
        if not length[len(k)]:                  # 아직 length에 없는거면 그대로 추가
            length[len(k)] = [k]
            continue
        key = length[len(k)][0]                 # length에 존재하면 몇번 나왔는지를 비교
        if dic[key] == v:                       # 같은 횟수면 추가
            length[len(k)] += [k]
        elif dic[key] < v:                      # 더 많이 나왔으면 덮어쓰기
            length[len(k)] = [k]
    # print(length)
    # length = {2: [('A', 'C')], 3: [('C', 'D', 'E')], 4: [('B', 'C', 'F', 'G'), ('A', 'C', 'D', 'E')]}

    answer = []
    for tups in length.values():
        for tup in tups:
            answer.append(''.join(list(tup)))
    answer.sort()
    return answer

print(solution(orders, course))
