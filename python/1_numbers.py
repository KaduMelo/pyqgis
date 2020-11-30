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

# Casting values
# int(), float, str()
# Use the int()
x = int(1)   # x will be 1
print(x)

y = int(2.8) # y will be 2
print(y)

z = int("3") # z will be 3
print(z)

# Use the float()
x = float(1)     # x will be 1.0 
print(x)

y = float(2.8)   # y will be 2.8
print(y)

z = float("3")   # z will be 3.0
print(z)

w = float("4.2") # w will be 4.2
print(w)

# Use the str()
x = str("s1") # x will be 's1'
print(x)

y = str(2)    # y will be '2'
print(y)

z = str(3.0)  # z will be '3.0'
print(z)

# (booleans, integers, floats, strings, and tuples) are immutable


