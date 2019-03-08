# SOME NOTES FOR STRINGS IN PYTHON


# Quotes or Double-quotes are the same for strings
name = "Andres"

same_name = 'Andres'

another_string = "alfabetica"


# Accessing position of a String
print(name[0])  # This will return the letter on position 0, in this case, A

# Get a substring (the second value is not considered on the returned string
print(name[2:5])  # This will return the string from position 2 included to position 5 excluded, in this case, dre

# Length of a String
print(len(name))  # This will return the length of the string, in this case, 6

# Lowercase
print(name.lower())  # This will return the whole string in lowercase, in this case, andres

# Uppercase
print(name.upper())  # This will return the whole string in uppercase, in this case, ANDRES

# Replacing letters
print(another_string.replace("a", "z"))  # This will return the same string but replacing "a" letter for "z" letter

# Input
x = input()  # This will require to enter a text to assign it to X variable
