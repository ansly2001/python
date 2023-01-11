'''Create a single string separated with space from two strings by swapping the
 character at position 1. '''

s1=input("enter the string1:")
s2=input("enter the string2:")
x=s1[0:1]
s1=s1.replace(s1[0:1],s2[0:1])
s2=s2.replace(s2[0:1],x)
print("the string after swapping:",s1,s2)