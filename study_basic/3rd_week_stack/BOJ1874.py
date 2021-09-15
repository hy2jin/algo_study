# BOJ 1874 스택 수열

N = int(input())
nums = list(int(input()) for _ in range(N))
idx = 0
stack, ans = [], []

for i in range(1, N+1):
    if not stack or stack[-1] != nums[idx]:
        stack.append(i)
        ans.append('+')
    if stack[-1] == nums[idx]:
        while idx < N and stack and stack[-1] == nums[idx]:
            stack.pop()
            ans.append('-')
            idx += 1

print('NO') if stack else print('\n'.join(ans))
