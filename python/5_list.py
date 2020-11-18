# Changeable
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
thislist = ["apple", "banana", "cherry"]
print(thislist)

# Allow Duplicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# List Length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

print (list1 + list2 + list3)

tudo_junto_e_misturado = list1 + list2 + list3
print (tudo_junto_e_misturado)

print((list1 + list2 + list3) == tudo_junto_e_misturado)

list1 = ["abc", 34, True, 40, "male"]
print(type(list1))

# Access Items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
print(thislist[-1])

# Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

# Range of Negative Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# Change Item Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1] = ["blackcurrant", "watermelon"]
print(thislist)

# Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# Add List Items
# append add in the end of the list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# index
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# Extend List
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Add Any Iterable
# pode ser iterable object (tuples, sets, dictionaries etc.).
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# Remove Specified Item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Passando index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# Sem passar index ele remove o último
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# Mostrar o erro que dá
thislist = ["apple", "banana", "cherry"]
del thislist
#print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# Loop Lists
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# Loop Through the Index Numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

# List Comprehension
# sintaxe menor
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# newlist = [expression for item in iterable if condition == True]

newlist = [x for x in range(10) if x < 5]
print(newlist)

# Sort
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Sort Descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# Copy Lists
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist.append("otherFruit")
print(mylist)

mylist = thislist.copy()
print(mylist)

# https://docs.python.org/3/tutorial/datastructures.html