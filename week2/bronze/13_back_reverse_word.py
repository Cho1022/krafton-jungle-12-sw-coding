import sys
input = sys.stdin.readline

a , b = input().split() #문장열 리스트로 저장된 a와 b가
rev_n = 0 #뒤집힌 숫자 담을 바구니

n = int(input()) 

while n > 0:
    # 1. n의 일의 자리 숫자 떼어내기 (예: 734 % 10 -> 4)
    mob = n % 10 
    # 2. 떼어낸 숫자를 rev_n에 이어 붙이기 (예: rev_n * 10 + 떼어낸 숫자)
    rev_n = rev_n * 10 + mob
    # 3. n의 일의 자리 잘라내기 (예: 734 // 10 -> 73
    n = n // 10 # 무한 루프 안되게 업데이트 해주기    
    

    
print(rev_n)