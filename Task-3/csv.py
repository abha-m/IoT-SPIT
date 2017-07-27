<<<<<<< HEAD
import csv
with open('f.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        #print(row)
        print(row[0])
=======
import csv
with open('f.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        #print(row)
        print(row[0])
>>>>>>> 6955c080d9a647ce01af530b8fbe5147aa14ca6b
        #print(row[0],row[1],row[2],)