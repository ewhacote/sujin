import sys
from collections import deque
input = sys.stdin.readline

def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append([numbers[0], 0])
    queue.append([-numbers[0], 0])

    while queue:
        tmp, idx = queue.popleft()
        if idx < len(numbers)-1:
            idx += 1
            queue.append([tmp + numbers[idx], idx])
            queue.append([tmp - numbers[idx], idx])
        else:
            if tmp == target:
                answer += 1

    return answer

if __name__ == "__main__":

    numbers = list(map(int, input().split()))
    target = int(input())

    print(solution(numbers, target))
