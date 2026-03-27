# 해시 테이블 - 세 수의 합 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2295
import sys

input = sys.stdin.readline
N = int(input())

# 1. N개의 숫자 입력받아 U에 채우기
U = [int(input()) for _ in range(N)]

# 2. 두 수의 합(x + y)을 모두 구해 주머니(Set)에 넣기
two_sums = set()
for x in U:
    for y in U:
        two_sums.add(x + y)

# 3. 큰 k부터 찾기 위해 내림차순 정렬
U.sort(reverse=True)

# 4. k와 z를 U에서 뽑아서, (k - z)가 주머니에 있는지 단번에 확인하기!
for k in U:
    for z in U:
        if (k - z) in two_sums:
            print(k)  # 가장 큰 k를 찾았으니 출력!
            exit()    # 프로그램 즉시 종료