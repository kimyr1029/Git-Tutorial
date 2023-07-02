#23122
n=int(input())
m=list(map(int,input().split()))
m.sort()
cnt=0
result=0
for i in m:
    cnt+=1 #모험가수포함
    if cnt>=i:
        cnt=0
        result+=1 #그룹수
   


print(result)