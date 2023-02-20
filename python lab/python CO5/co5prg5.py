import csv
cars=[{'no.':1,'company':'ferrari','model':'488GTB'},{'no.':2,'company':'bmw','model':'368GTB'},{'no.':3,'company':'porsche','model':'560GTB'}]
csvfile=open('Names.csv','w')
field_names=list(cars[0].keys())
writer=csv.DictWriter(csvfile,fieldnames=field_names)
writer.writeheader()
writer.writerows(cars)
csvfile.close()

csv_file=open('Names.csv','r')
csv_reader=csv.reader(csv_file)
for line in csv_file:
    print(line,end="")
csv_file.close()