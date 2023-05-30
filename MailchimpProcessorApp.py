import BaseModel
from LEADUtils import LEADPrinter
from kivy.uix.textinput import TextInput
import csv


# test some changes
class MailchimpProcessorApp:
    def start(self): 
        #leads = self.createLeads()

        #bankAccount_dict = self.createBankAccountDict(bankAccounts)
        #print(bankAccounts)
        #self.printBankAccountDict(bankAccount_dict)

        leadPrinter = LEADPrinter()
        leads = []
        leads = leadPrinter.readcsvandreturnlist()
        #lead_dict = self.createLeadDict(leads)
        #leadPrinter.printLeadDict(lead_dict)

        '''file = open('C:/Users/NAME/Downloads/segment_export_a63f2be7dd/n1.csv', encoding="utf8")
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
            iterator_c += 1'''
        #leadPrinter.printLeadList(leads)

        

              
           
    
        # set the created account owner object as the account owner of bank account 
       

mailchimprocessorApp = MailchimpProcessorApp()
mailchimprocessorApp.start()
