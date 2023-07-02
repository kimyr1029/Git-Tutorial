#
##
###
####
#####

#상하좌우
#2,2 2,1
dx=[0,0,-1,1]
dy=[-1,1,0,0]


n,k=map(int,input().split())
data=[]
for i in range(n):
    data.append(list(map(int,input().split())))

s,x,y=map(int,input().split())


def virus(x,y,n):
    for i in range(4):
        if x+dx[i]>=0 and x+dx[i]<n and y+dy[i]>=0 and y+dy[i]<n and data[x+dx[i]][y+dy[i]]==0:
            data[x+dx[i]][y+dy[i]]=n

cnt=0 #until s
spread=1 #until k
while(cnt<s):
    for i in range(n):
        if spread>k: 
            cnt+=1
            break
        for j in range(n):
            if data[i][j]==spread and spread<=k:
                virus(i,j,spread) #확산
                spread+=1

print(data[x-1][y-1])
            
            

    
