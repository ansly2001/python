l1=[1,2,3,4,5,6,7]
print("orginal list: ",l1)
for i in l1:
    if(i%2==0):
        l1.remove(i)
print("list after removing even numbers:",l1)