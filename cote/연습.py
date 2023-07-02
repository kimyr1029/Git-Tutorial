import sys
#input=sys.stdin.readline().strip()
k,p,n=map(int,input().split())
answer= k*(p**n)
print(answer%1000000007)
