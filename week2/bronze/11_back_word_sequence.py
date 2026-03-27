# <!-- https://www.acmicpc.net/problem/2675
# 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 
# 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. S의 길이는 적어도 1이며, 20글자를 넘지 않는다.  -->

# <!-- 
# 2
# 3 ABC        
# 5 /HTP

# AAABBBCCC
# /////HHHHHTTTTTPPPPP 
# -->

import sys 
input = sys.stdin.readline

#저장할 변수: tc, r, s, 누적변수ans 
#핵심조건: 반복횟수만큼 문자열을 어떻게 이어 붙일것인가.

N = int(input()) #testcase 2번-> 2줄이다. 
for tc in range(N):
# 입력: (한 줄에 들어오는 값을 어떻게 쪼갤 것인가?) 3 ABC 처럼
    r ,s   = input().split() #아예 문자열로 받아서 
    r = int(r) #  r만 수로 변환한다./ 
    ans = ""
# 출력: (최종적으로 무엇을 출력해야 하는가?)
#  print(ans)
# 저장할 상태: (테스트 케이스 수, 반복 횟수 R, 원본 문자열 S, 정답을 누적할 변수 등) 

# 반복 구조 후보: (입력받은 문자열의 각 문자를 순회하려면 어떤 for문이 필요한가?) 
    for cur in s:
        string = cur *  r
        ans += string
# 짧은 수도코드: (설명문이 아니라 코드 직전 단계의 실행 절차로 작성!) 
    print(ans) 
    # 테스트 케이스가 끝날 때 1회전 2회전 마다출력 하려면 tc안에 있어야 한다.
# 구조가 잡히면 아까 짜셨던 코드보다 훨씬 짧고 명확하게 풀릴 겁니다. 천천히 적