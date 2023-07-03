def recursive_factorial(n):
    if n==1:
        return 1
    else:
        return n*recursive_factorial(n-1)

def iterative_factorial(n):
    result = 1
    for i in range(1,n+1):
        result*=i
    return result

print("재귀적으로 구현 :", recursive_factorial(5))
print("반복적으로 구현 :", iterative_factorial(5))
