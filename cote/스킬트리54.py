#input
from collections import deque
def solution(skill, skill_trees):
    answer = 0
    # bef,cmp=-1,-1
    # leng=len(skill)
    # for skillt in skill_trees:
    #     bef,cmp=-1,-1
    #     for i in range(leng):
    #         if skill[i] in skillt:
    #             if bef!=-1:
    #                 if cmp!=-1:
    #                     bef=cmp
    #                     cmp=skillt.find(skill[i])
    #                 if cmp==-1:
    #                     cmp=skillt.find(skill[i])
                    
    #                 if bef>cmp: #스킬트리 에러
    #                     bef=-1
    #                     break
    #             if bef==-1 and i==0: #첫스킬을 못배우면 다른 스킬은 사용불가
    #                 bef=skillt.find(skill[i])
    #     if bef!=-1:
    #         answer+=1
    leng=len(skill)
    for skills in skill_trees: #목록
        skill_list=deque(skill[:]) #[a,b,c] 순서대로 리스트, q는 순차 pop 가능
        flag=0
        for s in skills:
            if s in skill and s!=skill_list.popleft(): 
                flag=-1
                break
        if flag==0:
            answer+=1

        

        
                
    return answer


print(solution("CBD",["BACDE","CBADF","AECB","BDA"]))