def solution(n,m,cards,numbers):
    answer = []
    cards.sort()
    for number in numbers:
        flag = '0'
        s,e = 0,n-1
        while s<=e:
            mid = (s+e)//2
            if cards[mid]<number:
                s=mid+1
            elif cards[mid]>number:
                e=mid-1
            else:
                flag = '1'
                break
        answer.append(flag)
    return " ".join(answer)

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
numbers = list(map(int, input().split()))

print(solution(n,m,cards,numbers))
