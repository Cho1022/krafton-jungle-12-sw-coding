class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# self.val = val: 노드가 저장하는 값   A칸 이라면 self.A 는 A칸의 숫자라고 생각하기
# self.next = next: 다음 노드를 가리키는 포인터 (기본값은 None)


def addTwoNumbers(l1, l2):
    dummy = ListNode(0)  # 결과 리스트의 시작점 역할을 할 가짜 노드
    curr = dummy
    carry = 0

    # 두 리스트 중 하나라도 남아있거나, 올림수(carry)가 있으면 계속 진행
    while l1 or l2 or carry:
        # 각 노드의 값을 가져오되, 노드가 없으면 0으로 처리
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        # 1. 현재 자릿수의 총 합 계산 (두 숫자 + 이전 올림수)
        total = val1 + val2 + carry

        # 2. 새로운 올림수 계산 (10 이상이면 1, 아니면 0)
        carry = total // 10

        # 3. 현재 자릿수에 기록할 값 계산 (10으로 나눈 나머지)
        out_val = total % 10

        # 결과 리스트에 새 노드 추가
        curr.next = ListNode(out_val)
        curr = curr.next

        # 다음 노드로 이동
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

        # 현재 자릿수의 총 합 계산 (두 노드의 값 + 이전 올림수)
    total = ++carry

    # 새로운 올림수(carry) 계산
    carry = total // 10

    # 현재 노드에 들어갈 실제 값 계산
    out_val = total % 10

    return dummy.next  # dummy 다음 노드부터가 진짜 결과물!
