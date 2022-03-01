# 2022 kakao blind recruitment 주차 요금 계산
'''
입차 후 출차되지 않으면 23:59에 출차된 것
'''

# 입차 시간, 출차 시간 계산
def time_diff(in_t, out_t):
    in_h, in_m = map(int, in_t.split(':'))
    out_h, out_m = map(int, out_t.split(':'))
    return (out_h*60+out_m) - (in_h*60+in_m)

def solution(fees, records):
    base_t, base_f, unit_t, unit_f = fees
    dic_in = {}                     # 차량번호: 입차 시간
    dic_ans = {}                    # 차량번호: 주차된 시간
    chk = set()                     # 출차 여부 판단
    for record in records:
        a, b, c = record.split()    # 시각, 차량번호, 내역
        if c == 'IN':
            dic_in[b] = a
            chk.add(b)
        else:
            chk.remove(b)
            diff = time_diff(dic_in[b], a)
            dic_ans[b] = dic_ans.get(b, 0) + diff

    # 출차 되지 않은 차량이 있으면
    if len(chk):
        for b in list(chk):
            diff = time_diff(dic_in[b], '23:59')
            dic_ans[b] = dic_ans.get(b, 0) + diff

    keys = sorted(dic_ans.keys())
    answer = []
    for k in keys:
        t = dic_ans[k]
        plus = 0
        if t > base_t:
            d, e = divmod(t - base_t, unit_t)
            if e: d += 1
            plus += d * unit_f
        answer.append(base_f + plus)

    return answer

a = solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
print(a)
