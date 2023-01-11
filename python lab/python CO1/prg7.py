#program7
l1=[2,3,4,5,7,8,6]
l2=[6,1,9,7]
s=int(0)
c=int(0)
if len(l1)==len(l2):
    print("length is same")
else:
    print("length is different")
for i in range(0,len(l1) and len(l2)):
    s=s+l1[i]
    c=c+l2[i]
if (s==c):
    print("sum of both list is same")
else:
    print("sum of both list are different")
print("element in same")
l=[]
for i in range(0,len(l1)):
    for j in range(0,len(l2)):
        if l1[i]==l2[j]:
            l.append(l1[i] and l2[j])
        else:
            continue
print(l)




            

