"""
[머지 정렬 구현]

문제 설명:
- 머지 정렬(Merge Sort) 알고리즘을 구현합니다.
- 분할 정복(Divide and Conquer) 방식을 사용합니다.
- 배열을 절반으로 나누고, 각각을 정렬한 후 병합합니다.

입력:
- arr: 정렬되지 않은 정수 배열

출력:
- 오름차순으로 정렬된 배열

예제:
입력: [38, 27, 43, 3, 9, 82, 10]
출력: [3, 9, 10, 27, 38, 43, 82]

힌트:
- 배열을 절반으로 분할 (재귀)
- 각 부분을 재귀적으로 정렬
- 정렬된 두 부분을 병합
"""


def merge(arr, left, mid, right):
    """
    두 개의 정렬된 부분 배열을 병합하는 함수
    """
    # 1. 왼쪽과 오른쪽 부분 배열을 임시 배열로 복사 (끝점에 +1 해주는 것 잊지 않으셨죠!)

    # 2. 정찰병 세팅
    i = 0  # left_arr의 카드를 가리킬 정찰병
    j = 0  # right_arr의 카드를 가리킬 정찰병
    k = left  # 원본 배열 arr에서 카드를 내려놓을 빈칸을 가리킬 정찰병

    # 3. 양쪽 배열 모두에 카드가 남아있는 동안, 카드의 '숫자'를 비교
    while i < len(left_arr) and j < len(right_arr):
        # 💡 [핵심 포인트] 아까 회원님이 left <= right 라고 쓰셨던 부분입니다.
        # 방 번호(인덱스)가 아니라, 정찰병이 들고 있는 실제 '카드 숫자'를 비교해야 합니다!
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]  # 왼쪽 카드가 작으면 원본 배열에 내려놓기
            i += 1  # 왼쪽 정찰병은 다음 카드로 이동
        else:
            arr[k] = right_arr[j]  # 오른쪽 카드가 작으면 원본 배열에 내려놓기
            j += 1  # 오른쪽 정찰병은 다음 카드로 이동

        k += 1  # 누가 이겼든 카드를 한 장 내려놓았으니, 원본 배열의 정찰병도 다음 빈칸으로 이동

    # 4. 남은 원소들을 복사 (메인 대결이 끝나고 남은 패를 다 털어넣는 과정)
    # left_arr에 남은 카드가 있으면 순서대로 다 복사
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    # right_arr에 남은 카드가 있으면 순서대로 다 복사
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1


def merge_sort_helper(arr, left, right):
    """
    머지 정렬 재귀 함수 (총괄 공장장)
    """
    # base case - 시작점이 끝점보다 작을 때만 (데이터가 2개 이상일 때만) 쪼개기 진행
    if left < right:
        # 1. 중간 지점 계산
        mid = (left + right) // 2

        # 2. 왼쪽 절반 재귀 정렬 (회원님이 +1 하셨던 부분 수정: mid까지만 딱 자릅니다)
        merge_sort_helper(arr, left, mid)

        # 3. 오른쪽 절반 재귀 정렬 (중간 바로 다음 칸부터 끝까지)
        merge_sort_helper(arr, mid + 1, right)

        # 4. 정렬된 두 절반을 병합
        merge(arr, left, mid, right)


def merge_sort(arr):
    """
    머지 정렬 메인 함수
    """
    if len(arr) > 1:
        # 최초 호출 시: 0번 인덱스부터 마지막 인덱스(길이 - 1)까지 총괄 공장장에게 넘김
        merge_sort_helper(arr, 0, len(arr) - 1)
    return arr


# 테스트 케이스 실행부
if __name__ == "__main__":
    arr1 = [38, 27, 43, 3, 9, 82, 10]
    print("=== 테스트 케이스 1 ===")
    print(f"정렬 전: {arr1}")
    result1 = merge_sort(arr1.copy())
    print(f"정렬 후: {result1}\n")

    arr2 = [12, 11, 13, 5, 6, 7]
    print("=== 테스트 케이스 2 ===")
    print(f"정렬 전: {arr2}")
    result2 = merge_sort(arr2.copy())
    print(f"정렬 후: {result2}")

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    arr1 = [38, 27, 43, 3, 9, 82, 10]
    print("=== 테스트 케이스 1 ===")
    print(f"정렬 전: {arr1}")
    result1 = merge_sort(arr1.copy())
    print(f"정렬 후: {result1}")
    print()

    # 테스트 케이스 2
    arr2 = [12, 11, 13, 5, 6, 7]
    print("=== 테스트 케이스 2 ===")
    print(f"정렬 전: {arr2}")
    result2 = merge_sort(arr2.copy())
    print(f"정렬 후: {result2}")
    print()

    # 테스트 케이스 3: 역순
    arr3 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("=== 테스트 케이스 3: 역순 ===")
    print(f"정렬 전: {arr3}")
    result3 = merge_sort(arr3.copy())
    print(f"정렬 후: {result3}")
    print()

    # 테스트 케이스 4: 중복 원소
    arr4 = [5, 2, 8, 2, 9, 1, 5, 5]
    print("=== 테스트 케이스 4: 중복 원소 ===")
    print(f"정렬 전: {arr4}")
    result4 = merge_sort(arr4.copy())
    print(f"정렬 후: {result4}")


