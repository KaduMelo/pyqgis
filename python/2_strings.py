# Immutable
# Declaração de uma variável do tipo String
# String são uma sequencia de caracteres, que pode entender como array
nome = "Kadu"
print(nome)

# Porque não imprimiu o resultado?
type(nome)

# Verificando o tipo da variável
print(type(nome))

# Explicar da que erro somar string com number
# print(nome + numero_int)
# print(nome + str(numero_int))

# Explicar que consegue pegar parte da string
# Que sempre o ultimo numero não aparece
print(nome[0:3])

print(nome[:3])

# Negativo index
print(nome[-3:-1])

# String length
print(len(nome))

# String Methods
# strip
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# lower
a = "Hello, World!"
print(a.lower())

# upper
a = "Hello, World!"
print(a.upper())

# replace
a = "Hello, World!"
print(a.replace("H", "J"))

# split
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# Check string
# in
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)

# Check string
# not in
txt = "The rain in Spain stays mainly in the plain"
x = "ain" not in txt
print(x)

# String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# String Format
age = 29
txt = "My name is Kadu, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# Named Indexes
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))

# Escape Character
# Mostrar o erro
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# https://docs.python.org/2.5/lib/string-methods.html

# (booleans, integers, floats, strings, and tuples) are immutable