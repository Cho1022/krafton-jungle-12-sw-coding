# https://www.acmicpc.net/problem/10807
#첫째 줄에 입력으로 주어진 N개의 정수 중에 v가 몇 개인지 출력한다.

import sys
input = sys.stdin.readline
N = int(input()) 
num_list = list(map(int, input().split()))
target = int(input())
cnt = 0

for cur in num_list:
    if cur == target:
        cnt += 1
#마법의 한문장: for문 전체가 이 아래 한문장으로 완성 
#cnt = num_list.count(target)

#현재수 와 target다르면 다음 수로 넘어가라
   # continue  없어도 파이선은 그냥 다음으로 알아서 넘어감
print(cnt)