n=input()

ln=len(n)
left=ln//2
right=ln
s1=0
s2=0
for i in range(left):
    s1+=int(n[i])
    s2+=int(n[i+left])

if s1==s2:
    print('LUCKY')
else:
    print('READY')