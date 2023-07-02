#먹방
#짧은시간부터 제거 전체시간(sum)>=((현재음식시간-이전음식시간)*음식갯수)--힙정렬
#다먹으면 음식갯수 줄어듬
#남은시간->2번반복
#
import heapq
def solution(food_times, k):
    ln=len(food_times)
    prev=0
    sum=0
    q=[]
    for i in range(ln):
        heapq.heappush(q,(food_times[i],i+1)) #시간순 정렬

    while(sum+((q[0][0]-prev)*ln)<=k): #앞에서부터 계산
        sum+=q[0][0]*ln
        prev=q[0][0]
        heapq.heappop(q)
        ln-=1
    result=sorted(q, key=lambda x:x[1]) #번호순정렬, #남은시간%남은갯수
    
    return result[(k-sum)%ln][1]

#q [row][col-0,1]
print(solution([3,1,2],5))