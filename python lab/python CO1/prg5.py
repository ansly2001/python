#Prompt the user for a list of integers.
n=int(input("enter the number of element:"))
l1=[]
for a in range(n):
    a=int(input("enter the number:"))
    if a>=100:
        l1.append('over')
    else:
        l1.append(a)
print("the output is",l1)