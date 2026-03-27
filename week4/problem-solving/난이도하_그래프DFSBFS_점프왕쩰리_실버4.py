# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173
import sys
input = sys.stdin.readline
N = int(input())

def dfs(r ,c ):
    jump = grid[r][c]
    
    next_moves = [(r + jump, c), (r, c + jump)] 
    
    for nr, nc  in next_moves: 
        # 빈칸 1: 지도 밖으로 나갔는지 확인 (나갔다면 건너뛰기)

        if nr >= N or nc >= N: 
            continue
        
        # (참고) 방문 기록 확인: 무한 루프 방지를 위해 이미 가본 곳은 건너뜁니다!
        if visited[nr][nc] == True:
            continue

        # 빈칸 2: 다음 칸이 목적지(-1)인지 확인 (도착했다면 탐색 성공!)
        if grid[nr][nc] == -1 : 
            return True
        #dfs 논리 적기 
    
        # ------------------------------------------
        # 모든 관문(지도 안쪽이고, 처음 가는 곳이고, 아직 도착 전)을 통과했다면?
        # 방문 기록을 남기고 다음 세계(좌표)로 깊게 파고듭니다!
        visited[nr][nc] = True
        if dfs(nr, nc) == True:
            return True

    # 아9래, 오른쪽 모두 가봤는데 길을 못 찾았다면 실패 반환
    return False

grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N  for _ in range(N)]
        
visited[0][0] = True
if dfs(0, 0) == True: #출발점 지정:
     print("HaruHaru")
else: 
     print("Hing")