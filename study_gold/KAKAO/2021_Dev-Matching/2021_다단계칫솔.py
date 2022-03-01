# 2021 Dev-Matching: 웹 백엔드 개발자 (다단계 칫솔 판매)

# enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
# referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
# seller = ["young", "john", "tod", "emily", "mary"]
# amount = [12, 4, 2, 5, 10]
# result = [360, 958, 108, 0, 450, 18, 180, 1080]

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["sam", "emily", "jaimie", "edward"]
amount = [2, 3, 5, 4]
# result = [0, 110, 378, 180, 270, 450, 0, 0]


def solution(enroll, referral, seller, amount):
    dic = dict(zip(enroll, referral))           # {사람: 추천인} 구조
    ans = dict(zip(enroll, [0]*len(enroll)))    # {사람: 이익} 구조

    for i in range(len(seller)):
        person = seller[i]
        price = amount[i] * 100         # 칫솔 개당 100원
        while True:
            ans[person] += price        # 판매
            if price < 10: break        # 추천인에게 줄 거 없음
            ten = int(price*0.1)        # 10% 계산
            ans[person] -= ten          # 10% 삭감
            person = dic[person]        # 추천인은 누구?
            if person == '-': break     # 추천없이 참여했으면 stop
            price = ten                 # 추천인이 있으면 가격 갱신하고 while
    return list(ans.values())

print(solution(enroll, referral, seller, amount))