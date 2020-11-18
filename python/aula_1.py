# COMEÇANDO A EXPLICAR INT
# Explicar o método print
# Declaração de uma variável do tipo int
numero_int = 3
print(type(numero_int))

print(numero_int)
print(id(numero_int))

# Somando com a variável
print(numero_int + 3)

# Variável continua com o mesmo valor
print(numero_int)
print(id(numero_int))

# Agora se somar colocando na mesma variável numero_int
numero_int = 3 + 3
print(numero_int)
print(id(numero_int))

# COMEÇANDO A EXPLICAR FLOAT
# Declaração de uma variável do tipo float
numero_float = 0.3
print(numero_float + numero_int)

# Declaração de uma variável do tipo complex
numero_complexo = 3.14j
print(type(numero_complexo))

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
print(nome + str(numero_int))

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

# Escape Character
# Mostrar o erro
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# https://docs.python.org/2.5/lib/string-methods.html
