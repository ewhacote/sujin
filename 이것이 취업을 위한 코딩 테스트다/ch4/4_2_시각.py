n=int(input())

def solution(n):
    answer = (n+1)*60*60
    for i in range(n+1):
        if "3" in str(i):
            continue
        for j in range(60):
            if "3" in str(j):
                continue
            for k in range(60):
                if "3" in str(k):
                    continue
                else:
                    answer-=1
    return answer

print(solution(n))