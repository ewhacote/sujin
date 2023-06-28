n,m,k = map(int,input().split())
numbers = list(map(int,input().split()))

def solution(n,m,k,numbers):
    answer = 0
    numbers.sort(reverse = True)
    first, second = numbers[0], numbers[1]

    i=0
    while True:

        for _ in range(k):
            answer += first
            m-=1
            if m==0:
                return answer
            
        for _ in range(1):
            answer += second
            m-=1
            if m==0:
                return answer

print(solution(n,m,k,numbers))