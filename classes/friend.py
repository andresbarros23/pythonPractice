from classes import contact


class Friend (contact.Contact):

    def __init__(self, name, email, phone):
        super.__init__(name, email)
        self.phone = phone
