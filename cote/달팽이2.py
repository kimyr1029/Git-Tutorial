import sys
input=sys.stdin.readline

n,m=map(int,input().split())
g=[[0]*m for _ in range(n)]

dx=[0,1,0,-1]
dy=[1,0,-1,0]
x,y=0,0
d=0
cnt=0
g[0][0]=1
while True:
    go=False #이동가능여부
    rot=False
    #회전
    for i in range(4):
        nx,ny=x+dx[d],y+dy[d] #이동        
        if 0>nx or nx>=n or 0>ny or ny>=m or g[nx][ny]==1:#회전
            d=(d+1)%4
            rot=True
            continue
        g[nx][ny]=1
        x,y=nx,ny
        go=True
        break

    if rot==True and go==True:
        cnt+=1
    if go==False:
        break
print(cnt)