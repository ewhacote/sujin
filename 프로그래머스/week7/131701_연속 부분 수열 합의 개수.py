def solution(elements):
    answer = []
    for l in range(1, len(elements)+1):
        for x in range(len(elements)):
            answer.append(sum(elements[:l]))
            elements = elements[1:] + elements[:1]
    
    return len(set(answer))
