# 스택 - 스택 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/10828
import sys

N = int(input())

s = []

for i in range(N):
    command = sys.stdin.readline().strip()

    if command[0:4] == "push":
        s.append(int(command[5:]))

    elif command == "pop":
        if len(s) >= 1:
            print(s[len(s) - 1])
            s.pop()
        else:
            print(-1)

    elif command == "size":
        print(len(s))

    elif command == "empty":
        if len(s) == 0:
            print(1)
        else:
            print(0)
    elif command == "top":
        if len(s) > 0:
            print(s[len(s) - 1])
        else:
            print(-1)