from classes import contactList


class Contact:

    all_contacts = contactList.ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)

