#회전
def rotate(a):
    n=len(a) #가로
    m=len(a[0]) #세로
    result=[[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1]=a[i][j]
    
    return result

#자물쇠중간체크
def check(new_lock):
    lock_length=len(new_lock)//3
    for i in range(lock_length,lock_length*2): #20~40
        for j in range(lock_length,lock_length*2): #20~40
            if new_lock[i][j]!=1:
                return False
    return True

def solution(key,lock):
    n=len(lock)
    m=len(key)

    new_lock=[[0]*n*3 for _ in range (n*3)] #3배변환

    #중앙부분에 자물쇠위치
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n]=lock[i][j]
    
    #4방향 회전
    for rotation in range(4):
        key = rotate(key)
        for x in range(n*2):
            for y in range(n*2):
                #자물쇠에 열쇠 끼워넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j]+=key[i][j]
                if check(new_lock)==True:
                    return True
                #자물쇠에 열쇠 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j]-=key[i][j]
    return False