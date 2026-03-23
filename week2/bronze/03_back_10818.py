# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
# 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.
# 입력:
# 5
# 20 10 35 30 7
# 출력: 7 35
import sys 
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))

max_val = num_list[0]
min_val = num_list[0]
# 이 문제를 조각내보면 20과 결국 다 비교 해야하고 10과 다 비교해야하고 결국 bruteforce방식 아닌가? 

for cur in num_list: 
    # # 같은 수일 경우도 생각하기
    # if cur  == max_val or cur == min_val:
    #     continue  
    if cur > max_val: 
        max_val = cur
    elif cur < min_val:
        min_val = cur
         
print(min_val, max_val)
print()

# 최솟값, 최대값은 이미 내장함수 있음 
# print(min(num_list), max(num_list) 이렇게 리스트 안에서  min , max 넣으면 알아서 출력