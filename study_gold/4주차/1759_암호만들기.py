# BOJ 1759 암호 만들기
import sys
sys.stdin = open('1759.txt')
'''
1. 최소 한개 모음 (a, e, i, o, u)
2. 최소 두개 자음
3. 오름차순 정렬
'''


def recur(cnt, si):
    if not cnt:     # 암호 완성
        ok = 0      # 모음수
        for tm in tmp:
            if tm in ('a', 'e', 'i', 'o', 'u'):
                ok += 1
        if ok and L-ok >= 2:        # (1)모음이 존재하고 (2)자음 두개 이상이면
            ans.append(''.join(tmp[::-1]))  # 뒤집혀있음
        return

    for idx in range(si, C):
        tmp[cnt-1] = word[idx]      # 뒤에서부터 채움
        recur(cnt-1, idx+1)


L, C = map(int, input().split())    # 암호는 L자리
word = sorted(input().split())      # C개의 알파벳, 오름차순(3)
tmp = [0]*L         # 암호
ans = []            # 암호 조건 만족함
recur(L, 0)
for an in ans:
    print(an)
