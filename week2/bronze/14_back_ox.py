# https://www.acmicpc.net/problem/8958

#OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고,
# X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.
# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.

# 입력: 첫째 줄에 테스트 케이스의 개수가 주어진다 + O/X 
# 출력: total_score , O이연속으로 나온다면, cnt로 수를 세고 더한다. 
# 반복 조건: 전체의 문자열을 순회한다. 
import sys
input = sys.stdin.readline
N = int(input())
for tc in range(N):
    #문자열 입력 받기 "ooxxox" 
    char = input() 
    cnt = 0 #
    total_score = 0
    for cur in char: #"ooxxox" 
        
        if cur == "O":
            cnt += 1 #
            total_score += cnt
        else: #X를 만난다면, 지금까지 cnt를 출력하고 초기화 
            cnt = 0    
    print(total_score)
