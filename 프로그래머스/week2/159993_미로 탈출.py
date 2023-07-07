import copy
from collections import deque

def bfs(maps,n,m,start,end):
    newmaps = copy.deepcopy(maps)
    queue = deque([start])
    newmaps[start[0]][start[1]]=0
    
    dx = [-1,1,0,0,]
    dy = [0,0,-1,1]
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m:
                if nx == end[0] and ny == end[1]:
                    return newmaps[x][y]+1
                if newmaps[nx][ny]=="O":
                    newmaps[nx][ny]=newmaps[x][y]+1
                    queue.append((nx,ny)) 
    return -1

def solution(maps):
    answer = 0
    
    n = len(maps)
    m = len(maps[0])
    
    for i in range(n):
        for j in range(m):
            if maps[i][j]=="L":
                lever = (i,j)
                
            if maps[i][j]=="S":
                start = (i,j)
                
            if maps[i][j]=="E":
                exit = (i,j)
    
    find_lever = bfs(maps,n,m,start,lever)
    if find_lever==-1:
        return -1
    find_exit = bfs(maps,n,m,start,exit)
    if find_exit==-1:
        return -1
    return find_lever + find_exit