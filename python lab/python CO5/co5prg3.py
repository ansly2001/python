import csv
csv_file=open("student detail1.csv")
csv_reader=csv.reader(csv_file)
for line in csv_file:
    print(line)