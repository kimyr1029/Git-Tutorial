n,m=map(int,input().split())

#무게별 개수 계산
#경우의수 => 무게갯수*남은공갯수
data=list(map(int,input().split()))
data.sort()
cnt=0
arr=[0]*(m+1)
for i in data:
    arr[i]+=1 #무게별개수

for i in range(m):
    n-=arr[i] #남은공개수
    cnt+=arr[i]*n #무게개수*남은공개수
# for i in range(n):
#     for j in range(i+1,n):
#         if arr[i]!=arr[j]:
#             cnt+=1

print(cnt)