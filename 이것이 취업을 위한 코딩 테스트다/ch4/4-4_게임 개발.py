n,m=map(int,input().split())
x,y,d=map(int,input().split())
envs=[]
for _ in range(n):
    envs.append(list(map(int,input().split())))

def solution(n,m,x,y,d,envs):
    answer = 0
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    while True:
        turned = 0
        for _ in range(4):
            d = (d-1)%4
            nx = x + dx[d]
            ny = y + dy[d]

            if 0<=nx<n and 0<=ny<m and envs[nx][ny]==0:
                envs[nx][ny]=-1
                x, y = nx, ny
                answer+=1
                break
            
            else: 
                turned+=1

        if turned==4:
            nx = x - dx[d]
            ny = y - dy[d]

            if 0<=nx<n and 0<=ny<m and envs[nx][ny]==1:
                return answer
            else:
                x, y = nx, ny


print(solution(n,m,x,y,d,envs))
