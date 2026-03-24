# https://www.acmicpc.net/problem/9086
# 입력: N =int(input()) for tc in range(N): 이런식으로 수를 받아야한다. 
# 출력: 문자열에서 인덱스[0] 첫글자를 꺼낸다. + 마지막 글자 인덱스 = len(문자열) - 1 이렇게 하면 될 거 같은데
# 인덱싱문법 [-1] 뒤에서 시작한다 == len(문자열) -1 
# 제한사항: 1~10까지만 tc가능 공백없음 split 안됨 int 안됌

import sys
input = sys.stdin.readline

N = int(input())
for tc in range(N): # N = 3 -> 0 ,1 2 
    #tc를 0회 1회 2회 하면서 문자열을 일렬로 받아야됨 
    string = input().strip() #문자열을 받아서 string에 저장 "받는다"== "저장한다"
    #"ABCD" -> 
    print(string[0] + string[-1])

    