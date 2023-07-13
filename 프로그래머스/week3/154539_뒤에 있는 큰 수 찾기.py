def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        bigger_number = -1
        j = i+1
        while j<len(numbers):
            if numbers[i]<numbers[j]:
                bigger_number = numbers[j]
                break
            else:
                j+=1
        answer.append(bigger_number)
                
    return answer
