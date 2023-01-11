currentyear=int(input("enter the current year:"))
finalyear=int(input("enter the final year:"))
for year in range(currentyear,finalyear):
    if(year%4==0):
        print("the leap year is:",year)