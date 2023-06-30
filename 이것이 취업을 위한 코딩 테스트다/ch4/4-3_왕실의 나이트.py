# ord() : 해당 문자의 유니코드 정수를 반환하는 함수
cmd = input()

def solution(cmd):
    answer = 0
    x,y = int(ord(cmd[0]))-int(ord('a'))+1,int(cmd[1])
    moves = [(2,1),(-2,1),(2,-1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]

    for dx, dy in moves:
        nx = x + dx
        ny = y + dy

        if 1<=nx<=8 and 1<=ny<=8:
            answer+=1
    
    return answer

print(solution(cmd))

    