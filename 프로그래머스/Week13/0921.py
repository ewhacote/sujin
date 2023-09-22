def to_balanced(p):
    cnt = 0
    for i in range(len(p)):
        if p[i]=="(":
            cnt+=1
        else:
            cnt-=1
        if cnt==0:
            return p[:i+1],p[i+1:]

def is_correct(p):
    cnt = 0
    for i in range(len(p)):
        if p[i]=="(":
            cnt+=1
        else:
            cnt-=1
    if cnt==0:
        return True
    else:
        return False
        
    
def solution(p):
    #1
    if len(p)==0:
        return ""
    
    #2
    u, v = to_balanced(p)
    
    #3
    if is_correct(u):
        return u+solution(v)
    
    
    #
    answer = ''
    return answer