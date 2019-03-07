# SOME NOTES FOR TUPLES IN PYTHON

# Ordered and Unchangeable. Allow duplicate members.

# Constructor

user_tuple = tuple(("Andres", "Ramon", "Eduardo"))

# Creation
this_tuple = ("juan", "pedro")

# Access
print(this_tuple[0])  # This will return the item 0 of the tuple

# Replace a value (NOT POSSIBLE)

# Loop
for x in this_tuple:
    print(x)


# Item presented
if "Andres" in this_tuple:
    print("Yes!!")


# Length
print(len(this_tuple))

# Add items (NOT POSSIBLE)

# Remove items (NOT POSSIBLE)

# Remove tuple

del this_tuple  # This will remove the tuple


# Count
this_tuple.count(2)  # This will return the number of times that 2 appears on the tuple

# Index
this_tuple.index(3)  # This will return the position of the specific value
