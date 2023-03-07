#데이터 중복이 많을수록 유용, count 초기화(max), sum
def count_sort(array):
    count=[0]*(max(array)+1)
    for i in range(len(array)):
        count[array[i]]+=1
#<-> count 0초기화, array값 index
    for i in range(len(count)):
        for j in range(count[i]):
            print(i,end=' ')

def count_sort(array):
    count=[0]*(max(array)+1)
    for i in range(len(array)):
        count[array[i]]+=1 #count만큼 출력
    for i in range(len(count)):
        for j in range(count[i]):
            print(i,end=' ')

def count_sort(array):
    count=[0]*(max(array)+1)
    for i in range(len(array)):
        count[array[i]]+=1
    for i in range(len(count)):
        for j in range(count[i]):
            print(i, end=' ')
def count_sort(array):
    count=[0]*(max(array)+1)
    for i in range(len(array)):
        count[array[i]]+=1
    for i in range(len(count)):
        for j in range(count[i]):
            print(i,end=' ')


