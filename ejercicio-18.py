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

@@ -33,24 +40,40 @@ def __str__(self):
    def showDeleted(self):
        st = ""
        printed = 0
        for contact in self.contacts:
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
        self.id = Contact.user_count
        self.id = str(Contact.user_count)
        self.name = name.upper()
        self.phone = phone
        self.state = True
        Contact.user_count += 1
        self.save()

    def save(self):
        Contact.ContactList.save(self)
@@ -64,6 +87,14 @@ def delete(self):

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
@@ -76,6 +107,7 @@ def addContact():
        return
    #We create a contact object
    contact = Contact(name, phone)
    contact.save()
    #We save it in "db"

def deleteContact():
@@ -99,13 +131,13 @@ def deleteContact():
    #In case he/she wants to find the user by ID
    elif option == "ID":
        try:
            contid = int(input("Type your contact's id: "))
            contid = input("Type your contact's id: ")
            Contact.ContactList.contacts[contid].delete()  
        except:
            #If it isn't valid it will restart
            print("The Id you typed wasn't valid, try again.")
            return deleteContact()
        #If ok get the contact and delete it
        Contact.ContactList.contacts[contid].delete()
    else:
        #If the option isn't valid it will restart
        print("The option you typed wasn't valid, try again")
@@ -127,30 +159,55 @@ def saveOnFile(dic):

def getFile():
    file = open(ruta, "r+")
    return loads(file.read())

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
    options = [addContact, deleteContact, listContacts, listDeleted , exit]
    try:
        screen = options[option]
        screen()
        return loads(file.read())
    except:
        print("Woops... Try again")

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