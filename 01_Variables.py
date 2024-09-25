# Variables
my_name = "Josafath"
print(my_name)

# Concatenaciones
my_int = 2002
print(my_int, "es el año que naci")
print(f"Soy {my_name} y tengo {my_int}")
print("Holaa tengo {}".format(my_int))
 
print("Hola soy ", my_name, "y tengo " + "22 años")

# Conversion a string
myInt_to_String = str(my_int)
print(myInt_to_String)

# Funciones del sistema
print(len("Hola"))
cadena = "hola"
print(cadena.upper())  # Salida: HOLA
cadena = "HOLA"
print(cadena.lower())  # Salida: hola
cadena2 = "Hola, mundo"
print(cadena2.replace("mundo", "Python"))
cadena = "Hola, mundo"
print(cadena.split())  # Salida: ['Hola,', 'mundo']
lista = ["Hola", "mundo"]
print(" ".join(lista))  # Salida: Hola mundo


# Variables en una sola linea
name, lastname, age = "Josafath", "Sosa", 21
print("Mi nombre es", name, lastname, "y tengo", age)


# Meter datos
# first_Name = input("¿Cual es tu nombre?")
# print(first_Name)

# ¿Forzamos el tipo?
adress: str = "Andalucia"
print(type(adress))
