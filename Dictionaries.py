# SOME NOTES FOR DICTIONARIES IN PYTHON

# Unordered, indexed and changeable. NO duplicate members.

# They have a key and a value <K, V>

# Constructor

user_dictionary = dict(brand="Ford", model="Focus", year=1942)

# Creation
this_dic = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Access
print(this_dic["brand"])  # This will return the value of the key "brand"

print(this_dic.get("brand"))  # This will return the value of the key "brand"

# Replace a value
this_dic["model"] = "Fiesta"  # This will put "Fiesta" on the value of "model" key, replacing the previous one.

# Loop
for x in this_dic:
    print(x)  # This will return the key values of the dictionary

for x in this_dic:
    print(this_dic[x])  # This will return the values of each key of the dictionary

for x in this_dic.values():
    print(x)  # This will return the values of each key of the dictionary

for x, y in this_dic.items():
    print(x, y)  # This will return each <K, V> of the dictionary


# Key presented
if "brand" in this_dic:
    print("Yes!!")


# Length
print(len(this_dic))

# Add items
this_dic["color"] = "Red"  # This will add a new <K, V> with the respective values.

# Remove items

this_dic.pop("color")  # This will remove the item with the specified key

this_dic.popitem()  # This will remove the last item inserted

del this_dic["model"]  # This will remove item with the key "model"

del this_dic  # This will remove the dictionary

# Clear
thislist.clear()  # This will clear the whole list, but it keeps existing

# Reverse
thislist.reverse()