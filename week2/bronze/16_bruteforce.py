# 체스판 

import sys 


str1 = "WBWBWBWB"
str2 = "BWBWBWBW"
pivot = [str1, str2] * 4

def sovle():
    N , M = map(int, input().split())
    board = []
    for _ in range(N):
        board.append(input())   
        
    ret = flaot('inf') 
    for i in range(a-N +1 ):
        for j in range(b-M +1):
            cnt = 0
            for k in range(N):
                for l in range(M):
                    if board[i+k][j+l] != pivot[i+k][j+l]: # 체스판과 다르면
                        cnt += 1 # 카운트 증가
            ret = min(ret, cnt) # 최소값 갱신하기
