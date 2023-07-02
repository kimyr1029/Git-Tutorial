def f(x):
    if x%2==0: return x+1

    res=list('0'+bin(x)[2:])
    idx=''.join(res).rfind('0')
    res[idx]='1'
    res[idx+1]='0'
    x=int(''.join(res),2)
    return x

def solution(numbers):
    return [f(number) for number in numbers]

print(solution([2,7]))