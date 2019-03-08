







c1 = Contact("Andres", "test@test.com")
c2 = Contact("Andres1", "test@test.com")
c3 = Contact("Andres2", "test@test.com")

c = Contact("John", "trr@tt.vo")

[print(c.name) for c in Contact.all_contacts.search('Andres1')]


s = Supplier("Peter", "test1@test.com")

