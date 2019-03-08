# SOME NOTES ABOUT PYTHON SPECIAL METHODS


# __init__
class First:
    """"__init__ method is the constructor of the class. Every object
    of this class must be created with those parameters (name and age)"""
    def __init__(self, name, age):
        self.name = name
        self.age = age


# __contains__
class Second:
    """"__contains__ method is to verify that the variables are not null"""
    a = "andres"

    def __init__(self, a):
        self.a = a

    def __contains__(self):
        if self.a:
            return True
        else:
            return False


# b = Second("peter")
# print(b.__contains__())
#
# c = Second("")
# print(c.__contains__())

a = list("andres")
b = list()
print(a.__contains__(b))
