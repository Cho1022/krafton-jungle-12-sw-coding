# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606

# 입력: 컴퓨터 수가 N개이고 몇쌍인지 M개를 입력 받는다.
# visited, cnt , 현제 감염된 번호 저장 변수 
# # 출력: 바이러스에 감염된 컴퓨터 수를 출력한다.(본인 제외)
# 제한: 

import sys
input = sys.stdin.readline
N  = int(input())
M = int(input())    

#전체 for문 필요 n , m 쌍이 graph에 있다는 것을 먼저 작성한다. 
graph = [[] for _ in range(N + 1)] #먼저 외운 문법 이 문법이 이렇게 [[], [], [], [], [], []] 틀을 만들고 이 안에 넣어야돼
visited =[False] * (N + 1)
cnt = 0 

for n , m in range(M): # (n, m) M개의 쌍을 받을 for문을 만든다.
    n , m = map(int,input().split())  # 이걸 통해서 쌍이 만들어지고    
    #입력을 받은 n, m을 어떻게 사용해야 할까? -> graph에 추가하는데 쌍으로 추가하기
    graph[n].append(m) #실질적으로 리스트 형태로 들어가는 부분은 여기
    graph[m].append(n) 
    
queue = deque() 
queue.append(1)
visited[1] = True
# 4. BFS 탐색 (이 부분을 직접 채워보세요!)
while queue:
    # 1) 큐에서 제일 앞에 있는 컴퓨터를 꺼내어 cur 변수에 담습니다.
    cur = queue.popleft()
    # 2) cur 컴퓨터와 연결된 이웃(nex)들을 반복문으로 확인합니다.
    for nex in graph[cur]:
        # 3) 만약 이웃(nex)을 아직 방문하지 않았다면?
        if visited[nex] == False:
            # 방문 스위치를 켭니다 (True로 대입).
            visited[nex] = True
            # 큐에 nex를 넣습니다.
            queue.append(nex)
            # 새롭게 감염되었으므로 cnt를 1 증가시킵니다.
            cnt += 1
# 5. 결과 출력 (1번 컴퓨터를 제외한 감염된 컴퓨터 수)
print(cnt)
    
    
cnt = 0 
def dfs(cur):
    global cnt
    visited[cur] = True 
    
    for nex in graph[cur]:
        if visited[nex] == False:
            cnt += 1 
            
            dfs(nex) #재귀요정 if문을 pass하면 방문한 것이니
            
dfs(1) #이게 논리적으로 이해가 안돼 설명에서는 이전부터 초기 시작을 1로 한다는 말이라는데 왜 맨 아래 return에서 하는건지 
