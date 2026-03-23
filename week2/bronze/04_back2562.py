# 예를 들어, 서로 다른 9개의 자연수
# 3, 29, 38, 12, 57, 74, 40, 85, 61
# 이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

# 입력: 9개의 수를 입력받고 각각 개행하기 N = map(int, input().split("\n")) 이렇게 하면 되려나? 
# 출력: 최대값 max_val, 최대값의[index] + 1 실제 수와 해서 맞추기
# 제한: 100보다 작다

import sys
input = sys.stdin.readline
max_val = 0 
num_list = [] # 이렇게 빈 리스트에 저장해서 9줄 만들 준비하기 

for _ in range(9): #0 ~ 8까지 9번 
    num_list.append(int(input())) #이렇게 한수씩 추가하기? 
max_val = max(num_list)
max_index = num_list.index(max_val) + 1 

print(max_val) 
print(max_index)