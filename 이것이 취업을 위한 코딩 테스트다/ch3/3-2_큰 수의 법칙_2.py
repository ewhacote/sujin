n,m,k = map(int,input().split())
numbers = list(map(int,input().split()))

def solution(n,m,k,numbers):
    numbers.sort(reverse = True)
    first, second = numbers[0], numbers[1]

    x = m//(k+1)*k + m%(k+1)
    y = m//(k+1)

    return x * first + y * second

print(solution(n,m,k,numbers))