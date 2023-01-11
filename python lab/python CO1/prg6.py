#Store a list of first names. Count the occurrences of ‘a’ within the list
names=['anu','john','hari']
count=0
for name in names:
    count=count+name.count('a')
    
print("the occurence of 'a'is: ",count)
    