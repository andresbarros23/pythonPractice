class ContactList(list):

    def search(self, name):
        """"Return all contacts that contain the search value
         in their name"""
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


class Contact:

    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)


class Supplier(Contact):

    def order(self, order):
        print("If this were a real system we would send "
              "'{}' order to '{}'".format(order, self.name))


class Friend (Contact):

    def __init__(self, name, email, phone):
        super.__init__(name, email)
        self.phone = phone

c1 = Contact("Andres", "test@test.com")
c2 = Contact("Andres1", "test@test.com")
c3 = Contact("Andres2", "test@test.com")

c = Contact("John", "trr@tt.vo")

[print(c.name) for c in Contact.all_contacts.search('Andres1')]


s = Supplier("Peter", "test1@test.com")

