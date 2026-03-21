# 트리 - 상근이의 여행 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/9372

#1. 첫 번째 줄에는 국가의 수 N(2 ≤ N ≤ 1 000)과 비행기의 종류 M(1 ≤ M ≤ 10 000) 가 주어진다.
#2. 이후 M개의 줄에 a와 b 쌍들이 입력된다. a와 b를 왕복하는 비행기가 있다는 것을 의미한다. (1 ≤ a, b ≤ n; a ≠ b) 
#3. 주어지는 비행 스케줄은 항상 연결 그래프를 이룬다.

import sys
input = sys.stdin.readline

# 힌트: for문을 한 번 더 써서 아무 변수에나 입력을 받아버리면 됩니다! 
T = int(input())
for _ in range(T):
    n , m = map(int, input().split())
    
    for _ in range(m):
        input() #여기가 그냥 입력 받는 부분입니다. -> 그리고 저장 안하면 날라감 
        
    print(n-1) # 트리의 간선의 개수는 항상 노드의 개수 -1 이므로 n-1을 출력해주면 끝    