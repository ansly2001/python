import calculator
a=int(input("enter the value of a: "))
b=int(input("enter the value of b: "))
choice=int(input("enter the choice:1.add 2.sub 3.mul 4.div"))
if choice==1:
    print(a,"+",b,"=",calculator.add(a,b))
elif choice==2:
    print(a,"-",b,"=",calculator.sub(a,b))
elif choice==3:
    print(a,"*",b,"=",calculator.mul(a,b))
elif choice==4:
    print(a,"/",b,"=",calculator.div(a,b))
else:
    print("no opertion")