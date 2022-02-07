def solution(id_list, report, k):
    n = int(k)
    answer = []

    # 누가 누구를 신고했는지
    dic = {id: set() for id in id_list}
    for rep in report:
        k, v = rep.split()
        dic[k].add(v)

    # 누가 몇번 신고당했는지
    x_dic = {id: 0 for id in id_list}
    for k in dic:
        for v in dic[k]:
            x_dic[v] += 1

    # 신고 횟수 이상인것만 남기기
    for k in dic:
        dic[k] = list(dic[k])
        for i in range(len(dic[k])-1, -1, -1):
            if x_dic[dic[k][i]] < n:
                dic[k].pop()
        answer.append(len(dic[k]))

    return answer

a = solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2)
print(a)