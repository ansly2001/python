# biggest of 3 numbers entered.
a=int(input("enter the first valve: "))
b=int(input("enter the second valve: "))
c=int(input("enter the third valve: "))
if a>b:
    if a>c:
        print("the biggest number is: ",a)
    else:
        print("the biggest number is: ",c)
else:
    print("the biggest number is: ",b)
        