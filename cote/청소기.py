#4방향불가 후진
#

n,m=map(int,input().split())
x,y,d=map(int,input().split())
g=[]
v=[[0]*m for _ in range(n)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]

for i in range(n):
    g.append(list(map(int,input().split())))
v[0][0]=1
cnt=1
while True:
    go=False
    for i in range(4): #방향이동(반시계)
        nx,ny=x+dx[(d+3)%4],y+dy[(d+3)%4]
        d=(d+3)%4
        if 0<=nx<n and 0<=ny<m and g[nx][ny]==0:#청소가능
            if v[nx][ny]==0:
                v[nx][ny]=1
                x,y=nx,ny
                go=True
                cnt+=1
                break
    if go==False: #4방향이동불가
        if g[x-dx[d]][y-dy[d]]==1: #후진불가
            print(cnt)
            break
        else:
            x,y=x-dx[d],y-dy[d]

