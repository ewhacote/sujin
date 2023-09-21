<<<<<<< HEAD
def correct(s):
    cnt = 0
    for i in s:
        if i == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    return cnt == 0
    
def divide(s):
    cnt = 0
    u = []
    v = []
    for idx,i in enumerate(s):
        u.append(i)
        if i == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            break
    for i in range(idx+1,len(s)):
        v.append(s[i])
    return [''.join(u),''.join(v)]
 
def rev(s):
    ret = ""
    dic = {
        "(" : ")",
        ")" : "("
    }
    for i in s:
        ret += dic[i]
    return ret
 
def dfs(s):
    if correct(s):
        return s
    u,v = divide(s)
    if correct(u):
        return u+dfs(v)
    else:
        return "(" + dfs(v) + ")" + rev(u[1:-1]) 
    
    
    
def solution(p):
    if p == "":
        return ""
    answer = dfs(p)
    return answer
=======
import math

def solution(w,h):
    return w*h - (w+h-math.gcd(w,h))
>>>>>>> 5175ca37bb18d0ca3f29960692f61e9d707bc473
