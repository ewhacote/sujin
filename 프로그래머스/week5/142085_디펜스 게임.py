from heapq import heappush, heappop

def solution(n, k, enemy):
    stage = len(enemy)
    
    # 모든 stage에서 무적권을 쓸 수 있는 경우
    if k >= stage :
        return stage
    
    q = []
    for i in range(stage):
        heappush(q,enemy[i])
        
        # 무적권이 부족한 경우
        if len(q) > k:
            least = heappop(q)
            
            # 병사가 부족한 경우
            if n < least : 
                return i
            # 병사가 충분한 경우
            n -= least
            
