def solution(targets):
    targets.sort(key=lambda x:x[1])
    answer = 0
    
    cut=0
    
    for s,e in targets:
        if s>=cut:
            cut=e
            answer+=1
              
    return answer