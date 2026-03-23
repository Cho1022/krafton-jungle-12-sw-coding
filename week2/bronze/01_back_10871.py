# https://www.acmicpc.net/problem/10871
# 제목: X보다 작은 수
# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
# 입력:
# 10 5
# 1 10 4 9 2 3 8 5 7 6
# 출력:1 4 2 3

N , X = map(int, input().split())   
num_list = list(map(int, input().split()))
#수를 하나씩 꺼내는 방법 이전 01번 부터 반복되는 법칙 암기
#result = []

for cur in num_list:
    
    if cur < X :
        #result.append(cur)
# else: continue 이렇게 안해도 파이썬은 다음으로 넘어감
    
#print(*result) unpacking문법  *붙이면됨
        print(cur , end =" ") #end = " " 설정으로 개행 안하고 띄어쓰기 가능
print()