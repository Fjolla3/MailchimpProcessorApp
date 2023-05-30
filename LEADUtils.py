import csv
import BaseModel

class LEADPrinter:

    def readcsvandreturnlist(self):
        file = open('C:/Users/DELL XPS/Downloads/segment_export_a63f2be7dd/n1.csv', encoding="utf8")
        csvReader = csv.reader(file)
        next(csvReader, None)

        leads = []
        iterator_c = 0
        for row in csvReader:
            if iterator_c > 3:
                break # we need the iterator if our CSV is longer than 50
            person_name = row[1]
            person_surname = row[2]
            person_email = row[0]
            person_no = row[3]

            Lead1 = BaseModel.Lead()
            Lead1.setFirstName(person_name)
            Lead1.setLastName(person_surname)
            Lead1.setPhoneNumber(person_no)
            Lead1.setEmail(person_email)
            leads.append(Lead1)

            #print(person_name +" "+ person_surname+" "+person_email+" "+person_no)
            iterator_c += 1
        
        return leads
    
    def datatabledata(self):
        file = open('C:/Users/DELL XPS/Downloads/segment_export_a63f2be7dd/n1.csv', encoding="utf8")
        csvReader = csv.reader(file)
        next(csvReader, None)

        leads = []
        iterator_c = 0
        for row in csvReader:
            if iterator_c > 23:
                break # we need the iterator if our CSV is longer than 50
            person_name = row[1]
            person_surname = row[2]
            person_email = row[0]
            person_no = row[3]

            leads.append((person_name, person_surname, person_no, person_email))

            #print(person_name +" "+ person_surname+" "+person_email+" "+person_no)
            iterator_c += 1
        
        return leads
        
class ATMImporter:
    # reads a csv file of bank accounts and print to terminal
    def importBankAccountsFromFile(self):
        # prepare csv file reading
        file = open('C:/Users/DELL XPS/Downloads/segment_export_a63f2be7dd/n1.csv', encoding="utf8")
        csvReader = csv.reader(file)
        next(csvReader, None)
        mailchimp_Subscribers = []
        
        # for each row of csvReader read the data direct into bankAccount 
        # and bank account owner objects
        for row in csvReader:
            mailchimpSubscribers = BaseModel.MailchimpSubscribers()

            mailchimpSubscribers.setEmail(row[0])
            mailchimpSubscribers.setPhoneNumber(row[3])

            mailchimpSubscribers.setFirstName(row[1])
            mailchimpSubscribers.setLastName(row[2])

            mailchimpSubscribers.setContactType(row[6])
            mailchimpSubscribers.setReason(row[7])
            mailchimpSubscribers.setEmployed(row[4])
            mailchimpSubscribers.setStudent(row[5])
            mailchimpSubscribers.setRegistrationDate('2023-01-01')
            mailchimpSubscribers.setCountry(row[8])


            # add each completed bank account object to bank accounts list
            mailchimp_Subscribers.append(mailchimpSubscribers)

        return mailchimp_Subscribers


o_list = []
ai = ATMImporter()
o_list = ai.importBankAccountsFromFile()

'''print("total number of objects: "+ str(len(o_list)))
print("First person Fists name: " + str(o_list[0].getFirstName()))
print("First person Last name: " + str(o_list[0].getLastName()))
print("First person Email : " + str(o_list[0].getEmail()))
print("First person Phone no: " + str(o_list[0].getPhoneNumber()))

print("First person Contact Type: " + str(o_list[0].getContactType()))
print("First person Student: " + str(o_list[0].getStudent()))
print("First person Employed: " + str(o_list[0].getEmployed()))
print("First person Reason: " + str(o_list[0].getReason()))
print("First person Country: " + str(o_list[0].getCountry()))'''