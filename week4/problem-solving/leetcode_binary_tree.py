from collections import deque
from typing import Optional, List

# LeetCode에서 기본으로 제공되는 노드 클래스 구조 (참고용)
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfLevels(self, root: Optional['TreeNode']) -> List[float]:
        # 1. 정답을 담을 바구니(리스트) 생성
        result = [] 
        
        # 큐를 생성하고, root 노드가 존재하면 큐에 넣고 시작
        queue = deque()
        if root:
            queue.append(root)
            
        # 2. 큐에 데이터가 있는 동안 계속 반복
        while queue: 
            # 3. 현재 레벨의 총 노드 개수
            level_node = len(queue)
            
            # 4. 현재 레벨의 합을 저장할 변수를 0으로 초기화
            level_sum = 0
            
            # 현재 레벨의 노드 개수만큼 정확히 반복
            for _ in range(level_node):    
                # 큐에서 제일 먼저 들어온 노드를 하나 뽑아서 node 변수에 저장
                node = queue.popleft()
                
                # 뽑은 노드의 '값(val)'만 level_sum에 더하기
                level_sum += node.val
                
                # 자식이 있는지 확인하고, 있으면 큐에 넣기
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            # 5. 레벨 반복문이 끝나면 (총합 / 노드개수)로 평균을 구해서 result에 추가
            result.append(level_sum / level_node)           
            
        # 6. 최종 정답 반환
        return result