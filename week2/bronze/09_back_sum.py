# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.

# 출력
# 입력으로 주어진 숫자 N개의 합을 출력한다.

import sys

input = sys.stdin.readline

sum_val = 0  # 전체 합을 저장할 global  변수설정
# 공백없이 입력받아서 이걸 문자열처럼 만들어서 더하는 방법 for사용하여 한글자씩

nums = input().strip()  # 54321 연속된 수를 입력 받고 -> 각 자리 수를 더한다.
for char in nums:
        # char에 저장되는 값은 [리스트로 한문자씩 저장된다.]
    sum_val += int(char)  # 이렇게 하면 계속 더하는 관계가 되지 않을까?
print(sum_val)
