# def select_sort(array):
#     for i in range(len(array)):
#         min=i
#         for j in range(i+1,len(array)):
#             if array[min]>array[j]:
#                    min=j
#         array[i],array[min]=array[min],array[i]
#     return array

# print(select_sort([1,5,3,11,4,2,7]))
#전체비교, min swap
def select_sort(array):
    for i in range(len(array)):
        min = i
        for j in range(i+1,len(array)):
            if array[min]>array[j]:
                min=j
        array[min],array[i]=array[i],array[min]
    return array

print(select_sort([1,5,3,11,4,2,7]))