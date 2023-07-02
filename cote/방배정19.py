import sys
sys.setrecursionlimit(2000)

def find_emptyroom(chk,rooms): #해당방데이터가없음, 새 방 할당이 가능
    if chk not in rooms:
        rooms[chk]=chk+1 #다음방이 비었다고 명시, 미리 다음 빈방을 명시
        return chk
    empty = find_emptyroom(rooms[chk],rooms) #1->2
    rooms[chk]=empty+1 #앞서 명시한 다음 방을 똑같이 따라감??
    return empty
# def find_emptyroom(chk,rooms):
#     if chk not in rooms:
#         rooms[chk]=1
#         return chk
#     return find_emptyroom(chk+1,rooms)
# 방이 빈 경우를 1부터 n까지 찾아야함 비효율

def solution(k,room_number):
    rooms=dict()
    for num in room_number:
        chk_in=find_emptyroom(num,rooms)
    return list(rooms)

print(solution(10,[1,3,4,1,3,1,1,2,3,4]))