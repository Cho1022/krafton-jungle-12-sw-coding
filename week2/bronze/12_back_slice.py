# https://www.acmicpc.net/problem/2908
# 입력: (무엇을 입력받나요? 두 수는 어떻게 주어지나요?)

import sys
input = sys.stdin.readline

a , b = input().split() #문장열 리스트로 저장된 a와 b가

ax = int(a[::-1]) #"123" -> "321" 뒤집힌 문자열 int()화 해야 정수로 비교 가능
bx = int(b[::-1]) 
max_val =0
#max_val = max(ax,bx)
if ax < bx:
    max_val = bx 
else: max_val = ax

print(max_val)