import sys

t=int(input())
dy=[1,0,-1,0]
dx=[0,-1,0,1]
d=0 #북서남동
ans=[]
for _ in range(t):
    x,y,mx,my,nx,ny=0,0,0,0,0,0
    d=0
    s=list(map(str,sys.stdin.readline().strip()))
    for i in s:
        if i=='F':
            x+=dx[d]
            y+=dy[d]
        elif i=='B':
            x-=dx[d]
            y-=dy[d]
        elif i=='L':
            d=(d+1)%4
        elif i=='R':
            if d==0:
                d=3
            else:
                d-=1

        mx=max(mx,x)
        my=max(my,y)
        nx=min(nx,x)
        ny=min(ny,y)
    ans.append(abs(mx-nx)*abs(my-ny))
for i in ans  :  
    print(i)