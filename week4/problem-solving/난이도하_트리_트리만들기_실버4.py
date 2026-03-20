# 트리 - 트리 만들기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/14244

import sys
input = sys.stdin.readline
# 두 수를 넣고 n = 5 m = 2
n , m = map(int, input().split())

# n - m =  2로 0 - 1 - 2 까지  연결 
for i in range(n - m):
    print(i, i +_1) 
#(0 ,1)
#(1, 2) 이렇게 출력 하면 성공

for j in range(n - m, n - 1):
    print(j, j + 1)
    