# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 1. 9개의 숫자를 입력받아 바구니에 담기
numbers = []
for _ in range(9):
    numbers.append(int(input()))

max_num = -1  # 세상에서 제일 작은 수로 일단 세팅 (누가 와도 첫 번째가 챔피언이 되도록)
max_index = -1  # 챔피언의 등번호(몇 번째인지)

for i in range(9): 
# TODO 1: 만약 현재 무대에 올라온 도전자( numbers[i] )가 기존 챔피언( max_num )보다 세다면(크다면)?
    if numbers[i] > max_num: 
    
# TODO 2: 칠판의 챔피언 점수( max_num )를 도전자 점수로 덮어씌운다!
       max_num = numbers[i]
# TODO 3: 칠판의 챔피언 등번호( max_index )를 도전자 번호로 덮어씌운다!
# (힌트: i는 0부터 시작하지만, 문제에서는 1번째 숫자부터 샌다고 했으니 i + 1 을 저장해야 합니다!)
       max_index = i + 1
       
    #혹은  max_num = max(numbers)
    #max_index = numbers.index(max_num) + 1 함수 사용도 가능

print(max_num)
print(max_index)