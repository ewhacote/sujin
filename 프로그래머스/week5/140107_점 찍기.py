def solution(k, d):
    answer = 0
    for a in range(d+1):
        for b in range(d+1):
            if (a*k)**2 + (b*k)**2 > d**2:
                break
            answer+=1
    return answer
