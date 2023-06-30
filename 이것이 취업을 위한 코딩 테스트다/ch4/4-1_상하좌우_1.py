n=int(input())
plans=list(input().split())

def solution(n,plans):
    x,y=1,1
    for plan in plans:
        if plan=="L" and 1<=y-1<=n:
            y-=1
        elif plan=="R" and 1<=y+1<=n:
            y+=1
        elif plan=="U" and 1<=x-1<=n:
            x-=1
        elif plan=="D" and 1<=x+1<=n:
            x+=1
        else:
            continue
    return str(x)+" "+str(y)

print(solution(n,plans))