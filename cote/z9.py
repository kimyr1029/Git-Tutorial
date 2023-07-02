def solution(s):
    #~len 압축,,
    answer=len(s)

    for step in range(1,len(s)//2+1): #1~6
        compressed=""
        prev=s[0:step] #0부터 step
        count=1
        for j in range(step,len(s),step): #1,2,3..
            if prev==s[j: j+step]: #step~2step
                count+=1
            else:
                if count>=2:
                    compressed+=str(count)+prev 
                else:
                    compressed+=prev
                prev=s[j:j+step] #초기화
                count=1
        if count>=2:
            compressed+=str(count)+prev 
        else:
            compressed+=prev
        answer=min(len(compressed),answer)
        
    return answer
    
print(solution('abcabcabcabcdededededede'))