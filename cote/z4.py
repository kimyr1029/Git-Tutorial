#1원부터 비교
#입력값먼저 비교
#입력값에 없으면 정렬상태에서 순차덧셈 비교

n=int(input())
m=list(map(int,input().split()))

m.sort()

#정렬 후
#1,2,3
#1 2 3 1+3 2+3 1+2+3 / 7(t)
#5->11 / 12(t)
#13->12(t)
#target=sum+1
target=1
for i in m:
    if target<i:
        #print(target)
        break
    else:
        target+=i

print(target)


# mx=sum(m)

# find=False
# for i in range(1,mx+1):
#     for j in m:
#         if i!=j:
#             continue
#         find=True
#     if find==False: #입력값없음        
#         for k in range(len(m)): #합산해서 찾기
#             add=0
#             for l in range(k,len(m)):
#                 add+=m[l] 
#                 if i==add: #합산하여 찾음
#                     find=True                
#                     break                
#                 if i!=add: 
#                     continue
#             if find==True: #찾았으면 다음 숫자 검색
#                 break
#     if find==False: #답찾음 탈출
#         print(i)
#         break        
#     find=False