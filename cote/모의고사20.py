def solution(answer):
    std1=[1,2,3,4,5] #0,1,2,3,4
    std2=[2,1,2,3,2,4,2,5] #0,1,2,3,4,5,6,7
    std3=[3,3,1,1,2,2,4,4,5,5] #0,1,2,3,4,5,6,7,8,9
    score=[0,0,0]
    result=[]
    #------enumerate idx%len(sss)
    for idx,answer in enumerate(answer):
        if answer==std1[idx%len(std1)]:
            score[0]+=1
        if answer==std2[idx%len(std2)]:
            score[1]+=1
        if answer==std1[idx%len(std2)]:
            score[2]+=1

    for idx,s in enumerate(score): #score
        if s==max(score):
            result.append(idx+1)
    return result