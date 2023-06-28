n=int(input()) #거슬러줘야 할 돈
coins=[500,100,50,10] #거스름돈의 종류

def solution(n,coins):
    answer = 0
    for coin in coins:
        answer+=n//coin
        n%=coin
    return answer

print(solution(n,coins))