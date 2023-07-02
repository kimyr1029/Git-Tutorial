def solution(number,answer):
    #cnt=0
    # while(True):
    #     if number==1 or cnt==500:
    #         break
    #     if number%2==0:
    #         number=number//2
    #     else:
    #         number=number*3+1

    #     cnt+=1

    # if number!=1:
    #     return -1
    # else:
    #     return cnt
    if number==1: return answer
    if answer==500: return -1

    if number%2==0:
        return solution(number//2,answer+1)
    else:
        return solution(number*3+1,answer+1)    
print (solution(6,0))