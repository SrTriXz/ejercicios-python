#crear una agenda de contactos
from io import open
import pathlib
from json import dumps, loads

filename = __file__.replace("py","json")
ruta = f"{pathlib.Path().absolute()}/{filename}"

class ContactList:
    @staticmethod
    def fromJson(dic):
        cl = ContactList()
        for id in dic:
            cl.contacts[id] = Contact.fromJson(dic[id])
        return cl

    def __init__(self):
        self.contacts = {}
    
    def save(self, contact):
        self.contacts[contact.id] = contact

    def getByName(self, name):
        for contact in self.contacts:
            if contact.name == name.upper() and contact.state:
                return contact
        return None
    def __str__(self):
        st = ""
        printed = 0
        for id in self.contacts:
            contact = self.contacts[id]
            if contact.state:
                st += f"{contact}\n"
                printed += 1
        if printed == 0:
            st = "There's no active contacts yet..."
        return st
    
    def showDeleted(self):
        st = ""
        printed = 0
        for id in self.contacts:
            contact = self.contacts[id]
            if not contact.state:
                st += f"{contact}\n"
                printed += 1
        if printed == 0:
            st = "There's no deleted contacts yet..."
        return st
    
    def toJson(self):
        dic = dict.copy(self.contacts)
        for id in dic:
            dic[id] = dic[id].toJson()
        return dic
class Contact:
    user_count = 0
    ContactList = ContactList()
    @staticmethod
    def fromJson(dic):
        contact = Contact(dic["name"], dic["phone"])
        contact.id = dic["id"]
        contact.state = dic["state"]
        return contact
    
    @staticmethod
    def updateUserCount(value):
        Contact.user_count = value

    def __init__(self, name, phone):
        self.id = str(Contact.user_count)
        self.name = name.upper()
        self.phone = phone
        self.state = True
        Contact.user_count += 1

    def save(self):
        Contact.ContactList.save(self)
        print(f"Your contact '{self.name}' has been saved successfully")
    

    def delete(self):
        self.state = False
        print(f"Your contact '{self.name}' has been deleted successfully")


    def __str__(self):
        return f"{self.id}) {self.name.upper()} | {self.phone}"
    
    def toJson(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "state": self.state
        }


def addContact():
    name = input("Type your new contact's name: ")
    if name == "..":
        return
    phone = input("Type your new contact's phone: ")
    #In case the user wanted to go back he/she can always type .. 
    if phone == "..":
        return
    #We create a contact object
    contact = Contact(name, phone)
    contact.save()
    #We save it in "db"

def deleteContact():
    option = input("Will you use its name or its id?: ").upper()
    #In case the user wanted to go back he/she can always type .. 
    if option == "..":
        return
    #In case he/she wants to find the user by name
    if option == "NAME":
        name = input("Type the name of the contact you don't want anymore: ")
        if name == "..":
            return
        #Gets the contact from the list
        contact = Contact.ContactList.getByName(name)
        #If it doesn't exist will restart
        if not contact:
            print("This contact doesn't exist, try again.")
            return deleteContact()
        #If ok delete
        contact.delete()
    #In case he/she wants to find the user by ID
    elif option == "ID":
        try:
            contid = input("Type your contact's id: ")
            Contact.ContactList.contacts[contid].delete()  
        except:
            #If it isn't valid it will restart
            print("The Id you typed wasn't valid, try again.")
            return deleteContact()
        #If ok get the contact and delete it
    else:
        #If the option isn't valid it will restart
        print("The option you typed wasn't valid, try again")
        return deleteContact()

def listContacts():
    print("\nYOUR CONTACTS: ")
    print(Contact.ContactList)
    
def listDeleted():
    print("\nYOUR PAST CONTACTS: ")
    print(Contact.ContactList.showDeleted())

def saveOnFile(dic):
    file = open(ruta, "w+")
    file.truncate()
    file.write(dumps(dic))
    file.close()

def getFile():
    file = open(ruta, "r+")
    try:
        return loads(file.read())
    except:
        return None

def InitialSettings():
    dic = getFile()
    if dic:
        Contact.ContactList = ContactList.fromJson(dic["contacts"])
        Contact.user_count = dic["user_count"]

def saveData():
    dic = {
        "contacts": Contact.ContactList.toJson(),
        "user_count": Contact.user_count
    }
    saveOnFile(dic)
    print("\nTu información ha sido guardada")

def finish():
    saveData()
    exit()


InitialSettings()
try:
    while True:
        option = input("""
        Choose an option:
        Add a contact       (0)
        Delete a contact    (1)
        List contacts       (2)
        List deleted        (3)
        Quit                (4)
        Note: You can always type '..' to go back
        :""").replace(" ", "")
        option = int(option)
        options = [addContact, deleteContact, listContacts, listDeleted , finish]
        try:
            screen = options[option]
            screen()
        except KeyboardInterrupt:
            finish()
        # except:
        #     print("Woops... Try again")
except KeyboardInterrupt:
    saveData()





