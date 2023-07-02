def solution(name):
    inp=['A' for _ in range(len(name))]
    #a-m:1~13
    #n-z:14~26
    cnt=0
    pos=0
    mov=0
    i=0
    visit=[0 for _ in range(len(name))]
    while(i<len(name)):
        #up/down
        if inp[pos]!=name[pos]:
            if ord(name[pos])>=ord('N'):
                cnt+=ord('Z')-ord(name[pos])+1
            else:
                cnt+=ord(name[pos])-ord('A')
        
        #left/right
        visit[pos]=1
        i+=1
        if pos+1<len(name):
            if visit[pos+1]==0 and name[pos+1]!='A':
                mov+=1
                pos+=1
        elif visit[pos-1]==0 and name[pos-1]!='A':
            mov+=1
            pos-=1
        
    return cnt+mov
print(solution("JEROEN"))