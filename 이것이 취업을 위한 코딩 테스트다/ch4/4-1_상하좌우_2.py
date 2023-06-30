n=int(input())
plans=list(input().split())

def solution(n,plans):
    x,y=1,1
    moves={"L":0,"R":1,"U":2,"D":3}
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    for plan in plans:
        i = moves[plan]
        nx = x + dx[i]
        ny = y + dy[i]

        if 1<=nx<=n and 1<=ny<=n:
            x,y=nx,ny
        else:
            continue
    
    return str(x)+" "+str(y)

print(solution(n,plans))