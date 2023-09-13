# https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    s = list(s)
    answer = [0, 0]
    while s != ['1']:
        c = len([x for x in s if x != '0'])
        answer[0] += 1
        answer[1] += len(s) - c
        
        s = []
        while c:
            s.insert(-1, str(c % 2))
            c //= 2
        
    return answer
