# 재귀함수 - 재귀함수가 뭔가요? (백준 실버5)
# 문제 링크: https://www.acmicpc.net/problem/17478

import sys
input = sys.stdin.readline

# 입력은 정수로 주어진다.
n = int(input()) # 재귀 깊이 입력받기
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.") # 첫 줄은 고정

# 2. 재귀 함수 정의하기 (재귀적으로 호출되는 함수)
def recursive(depth, n):
    #깊이에 맞게 언더바 생성 -> 깊이 * 언더바  
    under_bar = "____" * depth 
    
    # 1. base case: 종료 조건 -> 언제 멈추는가? 
    # -> depth가 n과 같아지는 순간 멈춘다. (재귀 깊이와 같아지는 순간)
    # 깊이가 n과 같아진다는 것은 질문이 n번 반복됐다는 의미이므로, 그 때 답변을 출력하고 재귀를 종료한다.
    if depth == n: 
        print(under_bar + '"재귀함수가 뭔가요?"') # 질문 출력
        print(under_bar + '"재귀함수는 자기 자신을 호출하는 함수라네"') # 답변 출력
        print(under_bar + '라고 답변하였지.') # 마지막 답변 출력
        return # 재귀 종료
    
    #2. 1회전 구현해 보기
    print(under_bar + '"재귀함수가 뭔가요?"') # 질문 출력
    print(under_bar + '"잘 들어보게. 옛날옛날 어느 한 지혜로운 삼촌이.. "') # 답변 출력
    print(under_bar + "'마을 사람들에게 많은 질문을 받았고, 그 선인에게 ...'")
    print(under_bar + "그의 답을 대부분 옳았다고 하네. 그런데 어느 날..")
    
    # 3. 재귀 호출하기 
    recursive(depth + 1 , n) # 재귀 호출 -> depth를 1 증가시켜서 다음 단계로 넘어가기
    print(under_bar + '라고 답변하였지.') # 재귀로 쌓인 함수들이 돌아오면서 마무리 출력하기
    
    
# 3. 재귀 함수 호출하기 (최초 호출)
recursive(0, n) # 최초 호출 -> depth는 0부터 시작, n은

"""
import sys

def recursive(depth, n):
    prefix = "____" * depth
    
    print(prefix + '"재귀함수가 뭔가요?"')
    
    if depth == n:
        print(prefix + '"재귀함수는 자기 자신을 호출하는 함수라네"')
    else:
        print(prefix + '"잘 들어보게. 옛날옛날 한 산 속에 머나먼 곳에 결정하는 재판관이 있었네.')
        print(prefix + '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
        print(prefix + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었네."')
        recursive(depth + 1, n)
        
    print(prefix + "라고 답변하였지.")

# 입력 받기
n = int(sys.stdin.readline())

# 시작 문구 출력
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")

# 재귀 함수 호출
recursive(0, n)
"""
