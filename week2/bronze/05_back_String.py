# https://www.acmicpc.net/problem/27866
# 입력: Sprout 
# 입력: 3 
# 출력: r 
# 문자열(String) 변수가 필요하고, 수를 입력 받을 변수 index가 필요한데 +1을해서 입력받는다. 
# 출력은 index를 반환하면된다. -> index를 반환하는거면 번호를 반환하니까, 단어[index]이렇게 출력을 써야한다.
# 숫자가 아니기 때문에 input는 int를 붙이지 않는다.

import sys
input = sys.stdin.readline

#string = list(input()) #문자열은 알아서 list로 감싸준다. 
string = input().strip() #strip()통해서 양쪽 개행 공백 삭제

n = int(input()) #입력받은 수는 인덱스 - 1 해야하고 그 인덱스 값을 출력한다. 
#직접 그려보면 왜 -1 인지 나온다. n =3 이라면 -> 인덱스[3] = o이다 따라서 -1 
print(string[n-1])