# https://school.programmers.co.kr/learn/courses/30/lessons/87946

from itertools import permutations
def solution(k, dungeons):
    answer = -1
    for dungeons in permutations(dungeons, len(dungeons)):
        hp = k
        temp = 0
        for s,e in dungeons:
            if hp >= s:
                hp -= e
                temp +=1
        if temp > answer : 
            answer = temp
                
    return answer