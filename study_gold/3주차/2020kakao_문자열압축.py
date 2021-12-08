def solution(s):
    n = len(s)
    answer = n
    for k in range(1, n//2 + 1):
        i = 0
        word = []   # 중복이 있는 문자열 (숫자형식으로 추가됨)
        cnt = 0     # 그 문자열이 몇개? (k 곱해서 빠짐)
        while i <= n-(2*k):
            if s[i:i+k] == s[i+k:i+2*k]:
                if not word or word[-1] != s[i:i+k]:
                    word.append(s[i:i+k])
                cnt += 1
            i += k
        answer = min(answer, n - (k*cnt) + len(word))
    return answer


inp = 'aaaabbcc'
print(solution(inp))
