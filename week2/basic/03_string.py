"""
[문자열 - 회문(Palindrome) 판별]

문제 설명:
- 주어진 문자열이 회문(앞에서 읽으나 뒤에서 읽으나 같은 문자열)인지 판별합니다.
- 대소문자를 구분하지 않고, 공백과 특수문자는 무시합니다.

입력:
- s: 판별할 문자열

출력:
- True: 회문인 경우
- False: 회문이 아닌 경우

예제:
입력: "A man, a plan, a canal: Panama"
출력: True

입력: "race a car"
출력: False

힌트:
- 알파벳과 숫자만 남기고 소문자로 변환하세요
- 문자열을 뒤집어서 비교하거나, 양 끝에서 시작해 중앙으로 이동하며 비교하세요
"""

def is_palindrome(s):
    """
    문자열이 회문인지 판별하는 함수
    
    Args:
        s: 판별할 문자열
    
    Returns:
        bool: 회문이면 True, 아니면 False
    """
    # TODO: 알파벳과 숫자만 남기고 소문자로 변환하세요
    # 힌트: isalnum() 메서드와 lower() 메서드 사용
    pass
    cleaned = ""
    # for char in s: #s에는"A man, a plan, a canal: Panama" 따라서 char로 받아야한다.
    #     if char.isalnum():#알파벳과 숫자만 남긴다. isalnum() True/False 반환하는데 if와 궁합으로 쓰인다.
    #         cleaned += char.lower() #문자열에서는 append가 아닌 "+" 를 사용한다. 소문자로 변환해서 cleaned에 추가한다.
    #     return cleaned_s == cleaned_s[::-1] #방법1
        
    # TODO: 정제된 문자열이 회문인지 확인하세요
    # 방법1: 문자열을 뒤집어서 비교 ([::-1] 사용)
    # 방법2: 양 끝 인덱스를 이용한 투 포인터 방식
    pass

    # 1. 알파벳과 숫자만 남기고 소문자로 변환 (전처리)
    for char in s:
        if char.isalnum():
            cleaned += char.lower()
            
    # 2. 투 포인터 출동!
    left = 0
    right = len(cleaned) - 1 
    
    while left < right:
        # 양쪽 글자가 다르면? 회문 탈락! (바로 False 퇴근)
        if cleaned[left] != cleaned[right]:
            return False
        
        # 같으면? 다음 글자를 검사하기 위해 손가락 한 칸씩 이동!
        left += 1
        right -= 1
        
    # while문을 중간에 안 쫓겨나고 무사히 다 끝마쳤다면? 완벽한 회문!
        return True
    
    
        # TODO 1: 만약 왼쪽 손가락이 가리키는 글자와 오른쪽 글자가 다르다면?
        # -> 바로 False를 return 하고 끝낸다!
    
        # TODO 2: 두 글자가 같다면 (위의 if문을 무사히 통과했다면), 다음 글자를 검사하기 위해 이동!
        # -> 왼쪽 손가락(left)은 1 더해주고,
        # -> 오른쪽 손가락(right)은 1 빼준다.
        
    # while문을 중간에 안 쫓겨나고 무사히 다 끝마쳤다면? 완벽한 회문입니다!
    
    #return False

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    test1 = "A man, a plan, a canal: Panama"
    result1 = is_palindrome(test1)
    print(f"입력: \"{test1}\"")
    print(f"회문 여부: {result1}")
    print()
    
    # 테스트 케이스 2
    test2 = "race a car"
    result2 = is_palindrome(test2)
    print(f"입력: \"{test2}\"")
    print(f"회문 여부: {result2}")
    print()
    
    # 테스트 케이스 3
    test3 = "Was it a car or a cat I saw?"
    result3 = is_palindrome(test3)
    print(f"입력: \"{test3}\"")
    print(f"회문 여부: {result3}")
    print()
    
    # 테스트 케이스 4
    test4 = "Madam"
    result4 = is_palindrome(test4)
    print(f"입력: \"{test4}\"")
    print(f"회문 여부: {result4}")


