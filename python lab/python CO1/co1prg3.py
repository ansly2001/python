# Generate positive list of numbers from a given list of integers
l1=[item for item in[0,3,2,-2,-3]if(item>=0)]
print("list is:",l1)

#Square of N numbers
square=[x*x for x in range(1,10)]
print("square are:",square)

#a list of vowels selected from a given word
l=[x for x in "apple" if x in ['a','e','i','o','u']]
print("list of vowels are:",l)

#List ordinal value of each element of a word
word=input("enter the string:")
l=[ord(i)for i in word]
print(l)