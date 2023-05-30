import csv
#import pandas as pd / we have to use it for near future

file = open('C:/Users/NAME/Downloads/segment_export_a63f2be7dd/n1.csv', encoding="utf8")
csvReader = csv.reader(file)

save_csv = []

iterator_c = 0
for row in csvReader:
    if iterator_c > 50:
        break#''' # we need the iterator if our CSV is longer than 50
    person_name = row[1]
    person_surname = row[2]
    person_email = row[0]
    person_no = row[3]
    person_contactType = row[4]


    #print(person_name +" "+ person_surname+" "+person_email+" "+person_no)
    save_csv.append([person_name, person_surname, person_email, person_no, person_contactType])
    iterator_c += 1

header = ['person_name', 'person_surname', 'person_email', 'person_no', 'person_contactType']
#data = ['James', 'Gosling', 'james.gosling@outlook.com', '++383123456']
with open("C:/Users/NAME/Desktop/test2.csv", 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    writer.writerows(save_csv)


file = open('C:/Users/DELL XPS/Desktop/test2.csv', encoding="utf8")
csvReader = csv.reader(file)

save_csv = []

iterator_c = 0
for row in csvReader:
    if iterator_c > 50:
        break#''' # we need the iterator if our CSV is longer than 50
    person_name = row[0]
    person_surname = row[1]
    person_email = row[2]
    person_no = row[3]
    person_contactType = row[4]


    print(person_name +" "+ person_surname+" "+person_email+" "+person_no+" "+person_contactType) 
    iterator_c += 1