import csv
persons=[('lata',22,45),('anil',21,56),('john',20,60),]
csv_file=open('persons.csv','w',newline="")
obj=csv.writer(csv_file)
for person in persons:
    obj.writerows(persons)
csv_file.close()
#obj.close()