# SOME NOTES FOR CLASSES IN PYTHON


# Creation
class FirstClass:
    x = 5


# Object creation
firstClassObject = FirstClass()


# Using object
print(firstClassObject.x)


# __init__() function
class SecondClass:
    """This is a docstring testing"""

    def __init__(self, name, age):  # This function is called every time the class is used to create an object
        self.name = name
        self.age = age

    def get_name(self):
        return self.name


secondClassObject = SecondClass("Andres", 26)



