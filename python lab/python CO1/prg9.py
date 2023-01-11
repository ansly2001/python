#Create a string from given string where first and last characters exchanged
text=input("enter a string: ")
newtext=text[-1]+text[1:-1]+text[0]
print("new string is:",newtext)