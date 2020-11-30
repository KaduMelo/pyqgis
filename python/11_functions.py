# Creating a Function
def my_function():
  print("Hello from a function")

my_function()

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

# error
# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil")

# * agrs
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# Keyword Arguments
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Default value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Passing a list as an argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# Return values
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# Recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

def imprimir_lista(A):
  for i in range(0,len(A)):
    print A[i]

def somar_elementos(lista):
  soma = 0
  for elemento in lista:
    soma = soma + elemento
  return soma

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(car.keys())
print("Chaves:", car.keys(), "Valores:", car.values(, end="\n"))

for key, value in car.items():
	print(key, ' : ', value)

# http://professor.ufabc.edu.br/~jesus.mena/courses/pi-1q-2013/caderno-de-exercicios-pi-em-python.pdf
