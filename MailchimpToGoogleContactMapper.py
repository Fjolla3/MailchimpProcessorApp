import BaseModel
import LEADUtils
import csv

class GContact:
    firstName = ""#
    lastName = ""#
    email1Type = ""#
    email1Value = ""#
    phone1Type = ""#
    phone1Value = ""#
    organization1Symbol = ""
    notes = ""#
    addres1Country = ""#
    organization1Name = ""
    organization1Title = ""
    Organization1Department = ""
    additionalName = ""
    birthday = ""
    subject = ""
    priority = ""

    def getFirstName(self):
        return self.firstName
    
    def setFirstName(self, firstName):
        self.firstName = firstName

    def getLastName(self):
        return self.lastName
    
    def setLastName(self, lastName):
        self.lastName = lastName

    def getPhone1Value(self):
        return self.phone1Value
    
    def setPhone1Value(self, phone1Value):
        self.phone1Value = phone1Value
    
    def getPhone1Type(self):
        return self.phone1Type
    
    def setPhone1Type(self, phone1Type):
        self.phone1Type = phone1Type

    def getEmail1Type(self):
        return self.email1Type
    
    def setEmail1Type(self, email1Type):
        self.email1Type = email1Type

    def getEmail1Value(self):
        return self.email1Value
    
    def setEmail1Value(self, email1Value):
        self.email1Value = email1Value
        
    def getAddres1Country(self):
        return self.addres1Country
    
    def setAddres1Country(self, addres1Country):
        self.addres1Country = addres1Country

    def getNotes(self):
        return self.notes
    
    def setNotes(self, notes):
        self.notes = notes
    
    ###organization1Symbol
    
    def getOrganizationSymbol(self):
        return self.organization1Symbol
    
    def setOrganizationSymbol(self, organization1Symbol):
        self.organization1Symbol = organization1Symbol
        
    def getOrganizationName(self):
        return self.organization1Name
    
    def setOrganizationName(self, organization1Name):
        self.organization1Symbol = organization1Name
        
    def getOrganizatioTitle(self):
        return self.organization1Title
    
    def setOrganizationTitle(self, organization1Title):
        self.organization1Title = organization1Title

    def getOrganizationDepartment(self):
        return self.Organization1Department
    
    def setOrganizationDepartment(self, Organization1Department):
        self.Organization1Department = Organization1Department

    def getAdditionalName(self):
        return self.additionalName
    
    def setAdditionalName(self, additionalName):
        self.additionalName = additionalName

    #####
    def getBirthday(self):
        return self.birthday
    
    def setBirthday(self, birthday):
        self.birthday = birthday

    def getPriority(self):
        return self.priority
    
    def setPriority(self, priority):
        self.priority = priority

    def getSubject(self):
        return self.subject
    
    def setSubject(self, subject):
        self.subject = subject

    pass

class MailchimpToGoogleContactMapper:
    def mapMailchimpSubscriberToGoogleContact(self, list_obj):
        
        googleContact_list = []
        for i in range(len(list_obj)):
            googleContact = GContact()

            googleContact.setFirstName(list_obj[i].getFirstName())
            googleContact.setLastName(list_obj[i].getLastName())

            googleContact.setPhone1Value(list_obj[i].getPhoneNumber())
            googleContact.setPhone1Type("Private")

            googleContact.setEmail1Type("Private")
            googleContact.setEmail1Value(list_obj[i].getEmail())

            googleContact.setNotes("WhatsApp")

            googleContact.setOrganizationSymbol("PO")
            googleContact.setOrganizationName("MM-GCh")
            googleContact.setOrganizationTitle("Lead")
            googleContact.setOrganizationDepartment("Coaching")

            googleContact.setAddres1Country("XK")

            googleContact.setBirthday("2001-09-03")
            googleContact.setPriority("Jo")
            googleContact.setSubject("Po")

            googleContact_list.append(googleContact)

        print("Convertion to google contact form MailchimpSubscriber csv is DONE!")

        return googleContact_list

    def gcontactcsv(self, list_obj):
        header = ['Name', 'Given Name', 'Family Name',	'E-mail 1 - Type',	'E-mail 1 - Value',	'Phone 1 - Type',	'Phone 1 - Value',	'Organization 1 - Symbol',	'Notes',	'Address 1 - Country',	'Organization 1 - Name',	'Organization 1 - Title',	'Organization 1 - Department',	'Additional Name', 'Birthday', 'Priority', 'Subject']#, 'email1_value', 'person_no']
        data = []
        for i in range(len(list_obj)):
            data.append([list_obj[i].getFirstName()+' '+ list_obj[i].getLastName(), list_obj[i].getFirstName(), list_obj[i].getLastName(),  list_obj[i].getEmail1Type(), list_obj[i].getEmail1Value(), list_obj[i].getPhone1Type(), list_obj[i].getPhone1Value(), list_obj[i].getOrganizationSymbol(), list_obj[i].getNotes(), list_obj[i].getAddres1Country(), list_obj[i].getOrganizationName(), list_obj[i].getOrganizatioTitle(), list_obj[i].getOrganizationDepartment(), list_obj[i].getAdditionalName(), list_obj[i].getBirthday(), list_obj[i].getPriority(), list_obj[i].getSubject()])
            pass
        with open("C:/Users/DELL XPS/Desktop/gconts.csv", 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)

            # write the header
            writer.writerow(header)

            # write the data
            writer.writerows(data)

        print("The CSV Google Contacts created from MailChimp csv!")
        print("#"*100)
        print(header)
        print("*"*100)
        print(data)

        pass
o_list = []
gc = []
ai = LEADUtils.ATMImporter()
o_list =  ai.importBankAccountsFromFile()
mtgcc = MailchimpToGoogleContactMapper()
gc = mtgcc.mapMailchimpSubscriberToGoogleContact(o_list)
mtgcc.gcontactcsv(gc)