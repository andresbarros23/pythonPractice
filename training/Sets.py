# SOME NOTES FOR SETS IN PYTHON

# Unordered and unindexed. NO duplicate members.

# Constructor

user_set = set(("Andres", "Ramon", "Eduardo"))

# Creation
this_set = {"juan", "pedro"}

# Access (NOT POSSIBLE SINCE IT IS UNINDEXED, YOU JUST CAN LOOP ON IT)

# Replace a value (NOT POSSIBLE)

# Loop
for x in this_set:
    print(x)


# Item presented
if "Andres" in this_set:
    print("Yes!!")


# Length
print(len(this_set))

# Add items
this_set.add("Sat")  # This will add that string to the set

this_set.update(["Orin", "Ded", "Andre"])  # This will add those strings to the set

# Remove items
this_set.remove("Andre")  # This will remove the item "Andre" of the set. If the item DOESN'T exist, we'll get an error

this_set.discard("Andre")  # This will remove the item "Andre" of the set. If the item DOESN'T exist, we won't get error

this_set.pop()  # This will remove the last item of the set. You don't know the item value since the set is unordered.

this_set.clear()  # This will clear the set


# Remove set

del this_set  # This will remove the set

