# SOME NOTES FOR LISTS IN PYTHON

# Ordered and changeable. Allow duplicate members.

# Constructor

user_list = list(("Andres", "Ramon", "Eduardo"))

# Creation
thislist = ["juan", "pedro"]

# Access
print(thislist[0])  # This will return the item 0 of the list

# Replace a value
thislist[0] = "Andres"  # This will put "Andres" on the position 0 of the list, replacing "Juan"

# Loop
for x in thislist:
    print(x)


# Item presented
if "Andres" in thislist:
    print("Yes!!")


# Length
print(len(thislist))

# Add items
thislist.append("John")  # This will add "John" at the end of the list

thislist.insert(2, "Peter")  # This will add "Peter" at position 2 of the list

# Remove items
thislist.remove("John")  # This will remove "John" from the list

thislist.pop()  # This will remove the last item of the list

thislist.pop(2)  # This will remove the item of position 2

del thislist[0]  # This will remove item 0 of the list

del thislist  # This will remove the list

# Clear
thislist.clear()  # This will clear the whole list, but it keeps existing

# Reverse
thislist.reverse()
