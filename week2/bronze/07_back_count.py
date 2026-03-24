# https://www.acmicpc.net/problem/2577
# # "숫자의 개수" 

# 리가 세어야 할 숫자는 0부터 9까지 연속된 숫자죠? 이럴 때는 딕셔너리보다 길이가 10인 리스트를 만들어두고,
# **'인덱스 = 찾아낸 숫자'**로 활용하는 '카운팅 배열(Counting Array)' 기법

# 입력: A, B, C (각 줄에 하나씩 정수)

# 출력: 0부터 9까지 각 숫자가 몇 번 쓰였는지 한 줄에 하나씩 출력 -> 세수의 곱 product ,0 ~ 9 회수 cnt

# 저장할 변수: (힌트: 숫자 0을 10개 가진 리스트 counts를 파이썬에서 가장 짧게 만드는 방법은 무엇일까요?)

# 반복 구조: 곱한 결과값(product)의 각 글자를 하나씩 순회 (1중 for문)

# 조건/갱신: (힌트: for문에서 방금 뽑아낸 글자를 인덱스로 삼아서, counts 리스트의 해당 위치 값을 1 증가시킨다고 한국어로 적어보세요.)

# 예상 시간복잡도: O(숫자의 길이)

import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

#1.counts를 길이 10짜리 0으로 초기화한다
counts = [0] * 10 

#2.product를 문자열로 바꾼 뒤 한 글자씩 순회한다
product = a * b * c 
for char in str(product):
    #한글자씩 꺼내는데 "7" -> 정수 7로 변환하기 
    # counts[int(char)] += 1
    digit = int(ch)
    count[digit] += 1   
    
    #counts배열 하나씩 출력하는 for문 구하기 
for cur in counts:
    print(cur)