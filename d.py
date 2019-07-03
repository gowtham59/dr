p1=int(input())
l2=[]
q3=[]
for i in range(p1):
    q3=list(map(int,input().split()))
    for j in range(len(q3)):
        l3.append(q3[j])
l2.sort()
for i in range(len(l2)-1):
    print(l2[i],end=' ')
print(l2[len(l2)-1])
