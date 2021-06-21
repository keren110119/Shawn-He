a=list(map(int,input().split()))
b=list(map(str,input().split()))
c=list(map(int,input().split()))
x=[]
for i in range(a[1]):
    if c[::2][i]!=c[1::2][i]:
        x.append(c[::2][i])

        if len(x)>=len(b):
            break
print(x)
for m in x:
    b.pop(m-1)
z=sorted(b)
n=list(map(str,z))

if len(b)>=1:
    print('Success! '+' '.join(n))
else:
    print('Fail!')