n,m=map(int,input().split())
graph=[[0]*m for _ in range(n)]
data=[]
for i in range(n):
    data.append(list(map(int,input().split())))

dx=[0,1,0,-1]
dy=[-1,0,1,0]
#방향이동
def virus(x,y):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        #북동남서 바이러스가 퍼질수있는 경우
        if nx>=0 or nx<n or ny>=0 or ny<m:
            if graph[nx][ny]==0: #빈칸 바이러스이동
                graph[nx][ny]=2
                virus(nx,ny) #바이러스 이동

#점수합산
def get_score():
    score=0
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                score+=1
    return score

#벽치기
def dfs(count):
    global result
    if count==3:
        for i in range(n):
            for j in range(m):
                graph[i][j]=data[i][j]
        
        for i in range(n):
            for j in range(m):
                if graph[i][j]==2: #바이러스 확산
                    virus(i,j)
        
        result=max(result,get_score())
        return
    
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0: 
                graph[i][j]=1
                count+=1
                dfs(count)
                graph[i][j]=0 #back??
                count-=1

dfs(0)
print(result)

