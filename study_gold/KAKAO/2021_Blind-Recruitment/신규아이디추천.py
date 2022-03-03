# 2021 Blind Recruitment 신규 아이디 추천

new_id = "...!@BaT#*..y.abcdefghijklm"
# result = "bat.y.abcdefghi"

# new_id = "z-+.^."
# result = "z--"

# new_id = "=.="
# result = "aaa"

# new_id = "123_.def"
# result = "123_.def"

# new_id = "abcdefghijklmn.p"
# result = "abcdefghijklmn"

'''
1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
'''
def solution(new_id):
    # 1
    new_id = new_id.lower()
    # 2
    rec_id = ''
    for w in new_id:
        if w.isalpha() or w.isdigit() or w in '-_.':
            rec_id += w
    # 3
    while '..'  in rec_id:
        rec_id = rec_id.replace('..', '.')
    # 4
    if rec_id and rec_id[0] == '.':
        rec_id = rec_id[1:]
    if rec_id and rec_id[-1] == '.':
        rec_id = rec_id[:-1]
    # 5
    if rec_id == '': rec_id += 'aaa'
    # 6
    if len(rec_id) > 15:
        if rec_id[14] == '.': rec_id = rec_id[:14]
        else: rec_id = rec_id[:15]
    # 7
    if len(rec_id) == 1:
        rec_id += rec_id[-1] * 2
    elif len(rec_id) == 2:
        rec_id += rec_id[-1]
    return rec_id

print(solution(new_id))