def solution(want, number, discount):
    answer = set()
    for i in range(len(discount)-10):
        
        during_membership = {}
        for saled_item in discount[i:i+10]:
            if saled_item not in during_membership:
                during_membership[saled_item]=0
            during_membership[saled_item]+=1
        
        for j in range(len(want)):
            if want[j] not in during_membership:
                continue
            if number[j]==during_membership[want[j]]:
                answer.add(j)
    print(answer)
    return len(answer)
