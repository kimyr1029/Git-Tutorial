def find(data,p,step): #사전, 현재문자열, 현재문자열숫자
    if step==6: return #종료조건
    if p!='': data.append(p)
    for c in ['A','E','I','O','U']:
        find(data,''.join([p,c]),step+1)#문자열연결

def solution(word):
    answer=0
    data=[]
    find(data,'',0)
    for i in range(len(data)):
        if data[i]==word:
            answer=i+1
            break
    return answer   

print(solution('AAAAE'))