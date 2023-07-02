n,m=map(int,input().split())
a=list(map(int,input().split()))
sum=a[0]
left=0
right=1
mx=0

i=0
while True:
    if right<m:
        sum+=a[right]
        right+=1
    else:
        left+=1
        mx=max(mx,sum)
        if right >=n:
            break
        sum=a[left]
        right=left+1
        m+=1
        
    
print(mx)        
    