from itertools import permutations
from itertools import combinations
from math import factorial
def solution(n,k):
    numbers=list(range(1,n+1))
    answer=[]
    k-=1 #index
    while numbers:
        idx,k = divmod(k,factorial(len(numbers)-1)) #몫 선택
        answer.append(numbers.pop(idx)) #선택된거 pop
    #return list(permutations([i+1 for i in range(n)],n))[k-1]
    return answer
print(solution(3,5))
