#fibonacci series of n numbers
#n=int(input("enter the number: "))
    
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
    
a=int(input("enter the number: "))
b=int(input("enter the number: "))
GCD=gcd(a,b)
print("GCD is:",GCD)