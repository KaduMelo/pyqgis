# Sets are used to store multiple items in a single variable.

# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

# A set is a collection which is both unordered and unindexed.

# Sets are written with curly brackets.

thisset = {"apple", "banana", "cherry"}
print(thisset)

# Duplicates Not Allowed
#thisset = ("apple", "banana", "cherry", "apple")

# print(thisset)

# Get the Length of a Set
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

# Set Items - Data Types
set1 = {"apple", "banana", "cherry"}
print(set1)

set2 = {1, 5, 7, 9, 3}
print(set2)

set3 = {True, False, False}
print(set3)

set1 = {"abc", 34, True, 40, "male"}
print(set1)

# type()
myset = {"apple", "banana", "cherry"}
print(type(myset))

# Access Items
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

# Add Items
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# Add Sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# Add Any Iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

# Remove Item
thisset = {"apple", "banana", "cherry"}

# da erro quando não encontra o item
thisset.remove("banana")

print(thisset)

# use in discard
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

# use the pop
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

# clear
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

# del
thisset = {"apple", "banana", "cherry"}

del thisset

# print(thisset)

# Loop item
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# Join Two Sets
# union
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# update
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# The intersection_update() method will keep only the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

# The intersection() method will return a new set, that only contains the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

# Keep All, But NOT the Duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(z)

# The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

# https://docs.python.org/3/library/stdtypes.html#set
