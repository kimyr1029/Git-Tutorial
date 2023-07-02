from collections import deque

n=int(input())
m=int(input())
mp=[[0]*(n+1) for _ in range(n+1)]
info=[]

for i in range(n):
    for j in range(n):
            mp[i][j]=0

for _ in range(m):
    a,b=map(int,input().split())
    mp[a][b]=1

dx=[0,1,0,-1]
dy=[1,0,-1,0]
#rotate=[('L',0,-1),('R',0,1),('U',-1,0),('D',1,0)]
q=deque()
r=int(input())
for _ in range(r):
    a,b=input().split()
    info.append((int(a),b)) #회전정보 시간 방향

cnt=0 #횟수저장
    #start
def turn(dir,c):
    if c=="L":
        dir=(dir-1)%4
    else:
        dir=(dir+1)%4

def simulate():
    x,y=1,1
    mp[x][y]=2 #뱀이 존재하는 위치 2로표시
    direction=0 #처음방향은 동쪽
    time=0 #저장할 시간
    index=0 #다음에 회전할 정보 0,1,,,
    q=[(x,y)] #뱀 위치정보
    while True:
        nx=x+dx[direction]
        ny=y+dx[direction]

        if 1<=nx and nx<=n and 1<=ny and ny<=n and mp[nx][ny]!=2: #맵 범위안에있고 이동위치에 뱀 몸통없다면
            if mp[nx][ny]==0:
                mp[nx][ny]=2 #꼬리->머리 이동
                q.append((nx,ny))
                px,py=q.pop()
                mp[px][py]=0
            if mp[nx][ny]==1: #사과존재-> 꼬리놔두고 머리 확장
                mp[nx][ny]=2 #꼬리->머리 이동
                q.append((nx,ny))
        else:
            time+=1 #벽이나 몸통 충돌
            break
        x,y=nx,ny #뱀 위치이동
        time+=1
        if index<1 and time==info[index][0]:
            direction=turn(direction,info[index][1])
            index+=1 #다음이동방향
        
    return time

print(simulate())
