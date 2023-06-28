n,m = map(int,input().split())
cards = []
for _ in range(n):
    cards.append(map(int,input().split()))

def solution(n,m,cards):
    mins = []
    for row in range(n):
        mins.append(min(cards[row]))
    return max(mins)

print(solution(n,m,cards))