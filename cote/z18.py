#괄호
#재귀
def balanced_index(p):
    count=0
    for i in range(len(p)):
        if p[i]=='(':
            count+=1
        else:
            count-=1
        if count==0:
            return i




