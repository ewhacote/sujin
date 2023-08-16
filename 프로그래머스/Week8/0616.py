def solution(cards):
    n = len(cards)
    global cnt
    answer = [0]
    visited=[0]*(n+1)
    
    for i in range(1,n+1):
        cnt=1
        if not visited[i]:
            visited[i]=1
            dfs(cards, i, visited)
            answer.append(cnt)
    answer.sort(reverse = True)
    return answer[0]*answer[1]

def dfs(cards, n, visited):
    global cnt
    if not visited[cards[n-1]]:
        visited[cards[n-1]]=1
        cnt+=1
        dfs(cards, cards[n-1], visited)