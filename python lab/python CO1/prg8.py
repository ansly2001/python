str=input("enter the string")
char=str[0]
str=str.replace(char,'$')
print(char+str[1:])