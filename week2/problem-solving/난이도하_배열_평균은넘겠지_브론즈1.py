# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344

# 1. 맨 처음 주어지는 테스트 케이스 개수를 받습니다.
C = int(input()) 

# 2. C번만큼 회원님의 코드를 반복 실행합니다.
for _ in range(C):
   
    data = list(map(int, input().split()))
    N = data[0] # N은 학생 수입니다. (첫 번째 숫자)
    scores = data[1:] # scores는 학생들의 점수입니다. (두 번째 숫자부터 끝까지)
    
    average = sum(scores) / len(scores)
    
    count = 0
    for num in scores:
        if num > average:
            count += 1
            
    # TODO: 방금 말씀드린 곱하기 100을 적용해서 rate 식을 완성해 보세요!
    rate = (count / N) * 1000
    print(f"{rate:.3f}%")