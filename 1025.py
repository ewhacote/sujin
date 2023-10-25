def solution(number, k):
    number = list(number)
    i = 0
    while k > 0:
        start = number[i] 
        end = number[i+1]
        if(start != end):
            if(start < end):
                del number[i]
                k -= 1
            else:
                del number[i+1]
                k -= 1
        else:
            i += 1
    return ''.join(number)
