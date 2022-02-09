# 2022 kakao blind recruitment 신고 결과 받기

def solution(id_list, report, k):
    n = int(k)
    answer = []

    dic = {id: set() for id in id_list}         # 누가 누구를 신고했는지
    for rep in report:
        k, v = rep.split()
        dic[k].add(v)
    # print(dic)

    x_dic = {id: 0 for id in id_list}           # 누가 몇번 신고당했는지
    for k in dic:
        for v in dic[k]:
            x_dic[v] += 1
    # print(x_dic)

    for k in dic:                               # 신고 횟수 부족한 경우 제외
        dic[k] = list(dic[k])
        for i in range(len(dic[k])-1, -1, -1):
            if x_dic[dic[k][i]] < n:
                dic[k].pop()
        answer.append(len(dic[k]))              # 몇번 연락받는가?
    return answer

a = solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2)
print(a)