#
# def insert_sort(array):
#     for i in range(1,len(array)):
#         for j in range(i,0,-1):
#             if array[j]<array[j-1]:
#                 array[j-1],array[j]=array[j],array[j-1]
#             else:
#                 break
#     print(array)
#1~len, i~0, j<j-1, swap
def insert_sort(array):
    for i in range(1,len(array)):
        for j in range(i,0,-1):
            if array[j]<array[j-1]:
                array[j-1],array[j]=array[j],array[j-1]
            else:
                break
    print(array)

insert_sort([6,1,5,3,11,4,2,7])
