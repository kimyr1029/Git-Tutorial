from collections import deque
def solution(number,k):
    answer=[]
    for num in number:
        while k>0 and answer and answer[-1]<num: #더큰숫자
            answer.pop() #버림
            k-=1
        answer.append(num)
        print(answer)
    return ''.join(answer[:len(answer)-k])
solution("4177252841",4)