# def quick_sort(array):
#     if len(array)<=1:
#         return array
    
#     pivot=array[0]
#     tail=array[1:]
#     left=[x for x in tail if x<=pivot]
#     right=[x for x in tail if x>pivot]

#     return quick_sort(left)+[pivot]+quick_sort[right]
# def quick_sort(array):
#     if len(array)<=1:
#         return array
    
#     pivot=array[0]
#     tail=array[1:]
#     left=[x for x in tail if x<=pivot]
#     right=[x for x in tail if x>pivot]
#     return quick_sort(left)+[pivot]+quick_sort(right)
# print(quick_sort([1,5,3,11,4,2,7]))
#len<=1 체크,pivot,나머지,비교 left,right 재귀
def quick_sort(array):
    if len(array)<=1:
        return array
    
    pivot=array[0]
    tail=array[1:]
    left=[x for x in tail if x<=pivot]
    right=[x for x in tail if x>pivot]
    return quick_sort(left)+[pivot]+quick_sort(right)

