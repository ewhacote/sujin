from collections import deque

def bfs(start, end, maps):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    n = len(maps)
    m = len(maps[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    que = deque()
    flag = 0
    
    # 시작점 탐색
    for i in range(n):
        for j in range(m):
        	# maps에 기록된 값이 "S"라면
            if maps[i][j] == start:      
                que.append((i, j, 0)) #(x,y,cost)   
                visited[i][j] = True
                flag = 1
                break 
        if flag: 
            break
                
    # BFS 알고리즘 수행
    while que:
        y, x, cost = que.popleft()
        
        if maps[y][x] == end:
            return cost
        
        # 상하좌우
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            # maps 범위내에서 벽이 아니라면 지나갈 수 있음
            if 0<= ny <n and 0<= nx <m and maps[ny][nx] !='X':
                if not visited[ny][nx]:	# 아직 방문하지 않는 통로라면
                    que.append((ny, nx, cost+1))
                    visited[ny][nx] = True
                    
    return -1	# 탈출할 수 없다면
        
            
def solution(maps):
    path1 = bfs('S', 'L', maps)	# 시작 지점 --> 레버
    path2 = bfs('L', 'E', maps) # 레버 --> 출구
    
    # 둘다 -1 이 아니라면 탈출할 수 있음
    if path1 != -1 and path2 != -1:
        return path1 + path2
        
   	# 둘중 하나라도 -1 이면 탈출할 수 없음
    return -1