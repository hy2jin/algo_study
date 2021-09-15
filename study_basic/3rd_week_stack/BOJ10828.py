# BOJ 10828 스택
import sys
read = sys.stdin.readline
N = int(read())
st = []
for _ in range(N):
    tmp = read()
    if tmp[0] == 'p':
        if tmp[1] == 'o':
            print(st.pop()) if st else print(-1)
        else:
            st += [tmp.split()[1]]
    elif tmp[0] == 's':
        print(len(st))
    elif tmp[0] == 'e':
        print(1) if not st else print(0)
    else:
        print(st[-1]) if st else print(-1)