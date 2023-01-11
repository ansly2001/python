#Print out all colors from color-list1 not contained in color-list2. 
l1=['red','black','blue','green']
l2=['yellow','red','pink']
a=[x for x in l1 if x not in l2 ]
print("the colors are:",a)

            