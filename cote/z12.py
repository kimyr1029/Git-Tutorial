def possible(answer):
    for x,y,stuff in answer:
        if stuff==0: #xy^ 기둥 xy0
            if y==0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            return False
        elif stuff ==1:#xy1> 보
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or [x-1,y,1] in answer or [x+1,y,1] in answer:
                continue
            return False
    return True

def solution(n,build_frame):
    answer=[]
    for frame in build_frame:
        x,y,stuff,operate=frame
        if operate ==0:
            answer.remove([x,y,stuff])
            if not possible(answer):
                answer.append([x,y,stuff])
        elif operate==1:
            answer.append([x,y,stuff])
            if not possible(answer):
                answer.remove([x,y,stuff])
    
    return sorted(answer) #정렬결과 반환

