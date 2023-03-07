#정렬된상태, start<=end---//2 target 나올때까지
def binary_search(array,target,start,end):
    while start<=end:
        mid=(start+end)//2
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end=mid-1
        elif array[mid]<target:
            start=mid+1
    return None
#원소개수, 타겟
n, target=map(int,input().split())
array=list(map(int,input().split())) 

result=binary_search(array,target,0,n-1)
if result==None:
    print('원소가 존재하지 않습니다.')
else:
    print(result+1)

import sys
input_data=sys.stdin.readline().rstrip()

def binary_search(array,target,start,end):
    while start<=end:
        mid=(start+end)//2
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return None

n,target=map(int,input().split())
array=list(map(int,input().split()))
result=binary_search(array,target,0,n-1)
if result==None:
    print('없음')
else:
    print(result+1)