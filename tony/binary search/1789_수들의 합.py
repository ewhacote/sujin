def solution(s):
    nsum, i = 1, 1
    while nsum<=s:
        i+=1
        nsum+=i
    return i-1

s = int(input())
print(solution(s))
