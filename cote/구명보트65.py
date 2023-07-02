def solution(people,limit):
    people.sort()
    answer=0
    a=0
    b=len(people)-1
    #투포인터   <-   >
    while a<b:
        if people[b]+people[a]<=limit:
            a+=1
            answer+=1
        b-=1
        
    return len(people)-answer #합석

solution([70,80,50],100)