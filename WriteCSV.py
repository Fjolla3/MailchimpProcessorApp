import csv

header = ['Name', 'given_name', 'family_name', 'email1_value', 'person_no']
data = ['Fio', 'Fio Hal', 'Hal','fio_hal@live.com', '+383111222']
with open("C:/Users/DELL XPS/Downloads/gcontacts-mailchimp-jcoaching.csv", 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    writer.writerow(data)

on_no = row[3]

    print(Name +file = open('C:/Users/NAME/Downloads/gcontacts-mailchimp-jcoaching.csv', encoding="utf8")
csvReader = csv.reader(file)
for row in csvReader:
    '''if iterator_c > 50:
        break''' # we need the iterator if our CSV is longer than 50
    Name = row[1]
    given_name = row[2]
    family_name = row[4]
    email1_value = row[0]
    pers" "+ given_name+" "+email1_value+" "+person_no)