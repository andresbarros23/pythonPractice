# SOME NOTES FOR LOOPS IN PYTHON

# We have two kind of loops: FOR and WHILE

# WHILE
i = 1
while i < 6:
    print(i)
    i += 1  # It's important to increment the indexed variable or the loop will continue forever
    if i == 3:
        break  # When this condition is met, the loop is stopped.

    if i == 4:
        continue  # When this condition is met, the loop continue with the following iteration


# FOR
for x in "andres":
    print(x)

    if x == "e":
        break

    if x == "a":
        continue


# range function
for x in range(10):  # Range function returns a sequence of numbers, from 0 to the specified number, incrementing 1.
    print(x)

for x in range(2, 6):  # Remember that the last number is not included.
    print(x)

for x in range(2, 36, 2):  # The last parameter indicates the increment value
    print(x)

# else block
for x in "banana":
    print(x)
else:
    print("loop finished")  # After the loop finishes, the else block is executed.


# Inner loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:

    for y in fruits:
        print(x, y)

