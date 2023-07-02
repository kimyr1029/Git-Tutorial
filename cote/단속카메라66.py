def solution(routes):
    routes=sorted(routes,key=lambda x:x[1]) #출구시점

    idx=len(routes)
    i=0
    cnt=0
    last=-30001
    while(i<idx):
        if last<routes[i][0]: #감시범위 벗어남
            cnt+=1
            last=routes[i][1] #설치위치
        i+=1
    
    return cnt

print(solution([[-20,-15],[-14,-5],[-18,-13],[-5,-3]]))             