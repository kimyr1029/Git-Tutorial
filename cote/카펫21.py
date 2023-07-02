def solution(brown,yellow):
    width,height=0,0
    #1,4,9,16,25,36,49
    #8,1
    #1:8,2:10,3:12, 
    #n*m(가로세로)
    grid=brown+yellow #3~4
    for n in range(3,int(grid**0.5)+1): #최소 길이부터 정사각형까지
        if grid % n != 0: continue #몫
        m=grid//n
        if (n-2)*(m-2) == yellow: #전체 area, 가로세로(-2)
            return[m,n]