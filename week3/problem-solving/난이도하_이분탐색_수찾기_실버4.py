# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920
import sys

input = sys.stdin.read().split()

n = int(input[0])

# 탐색 대상 집합 (중복 제거 및 O(1) 탐색을 위해 set 사용)
a = set(input[1:n+1])

m = int(input[n+1])
targets = input[n+2:]

# 존재 여부에 따라 1 또는 0 출력
for x in targets:
    if x in a:
        print(1)
    else:
        print(0)