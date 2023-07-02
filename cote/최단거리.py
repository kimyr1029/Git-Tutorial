from collections import deque

# def solution(maps):

#     width,height=len(maps[0]),len(maps)
#     paths=[[-1,0],[0,1],[1,0],[-1,0]]
    
#     def bfs(x,y,cost,path):
#         q=deque()
#         q.append((x,y,cost,path))
#         visit=[[0]*width for _ in range(height)]
                
#         cnt=0
#         while q:
#             x,y,c,p=q.popleft()
#             for i in range(len(paths)):
#                 nx=x+paths[i][0]
#                 ny=y+paths[i][1]
                                
#                 if nx>=0 and nx<height and ny>=0 and ny<width:
#                     if i==path:
#                         nc=c+100
#                     else:
#                         nc=c+600     
#                     if maps[nx][ny]==0 and visit[nx][ny]==0 :
#                         visit[nx][ny]=nc
#                         q.append((nx,ny,nc,i))
#                     elif maps[nx][ny]==0 and visit[nx][ny]!=0:
#                         if nc<visit[nx][ny]:
#                              visit[nx][ny]=nc
#                              q.append((nx,ny,nc,i))
#         return visit[width-1][height-1]
#     return min(bfs(0,0,0,1),bfs(0,0,0,2))
def solution(board):
    size=len(board)
    paths=[(-1,0),(0,-1),(1,0),(0,1)]
    def bfs(x,y,cost,path):
        graph=[[0]*size for _ in range(size)]
        for a in range(size):
            for b in range(size):
                if board[a][b]==1: graph[a][b]=-1 #벽
        q=deque()
        q.append((x,y,cost,path))

        while q:
            x,y,cost,path=q.popleft()
            for i in range(len(paths)):
                nx=x+paths[i][0]
                ny=y+paths[i][1]

                if nx<0 or nx>=size or ny<0 or ny>=size or graph[nx][ny]==-1:
                    continue
                if path ==i:newcost=cost+100
                else: newcost=cost+600

                if graph[nx][ny]==0 or (graph[nx][ny]!=0 and graph[nx][ny]>newcost):
                    q.append((nx,ny,newcost,i))
                    graph[nx][ny]=newcost
        return graph[size-1][size-1]
    return min(bfs(0,0,0,2),bfs(0,0,0,3))
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
        