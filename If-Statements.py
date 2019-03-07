# SOME NOTES FOR IF STATEMENTS IN PYTHON

# We use logical conditions for this statements

a = 33
b = 44

# Example
if a > b:
    print("Testing if statement")
elif a < b:
    print("Testing elif statement")
else:
    print("Testing else statement")


# Short IF
if a == b: print("Testing short if")

# Short IF...ELSE
print("A") if a > b else print("=") if a == b else print("B")

