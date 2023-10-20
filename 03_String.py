#Strings#

my_string = "Hola josa"
my_other_string = "como estas"

print(my_string + " " + my_other_string)

my_string_linea = "Hola \n¿como estas?"
print(my_string_linea)

my_string_tabulacion = " \t Hola"
print(my_string_tabulacion)

#Formateo

name, lastname = "Josafath", "Sosa"

print("Mi nombre es {} {}".format(name, lastname))
print("Su nombr es %s %s" %(name, lastname))
print(f"Mi nombre es {name} {lastname}")

#Desempaqetado de caracteres
lenguage = "pyThon"
a,b,c,d,e,f = lenguage

print(c)
print(f)

#División
lenguage_slice = lenguage[0:6]
print(lenguage_slice)
lenguage_slice = lenguage[3:]
print(lenguage_slice)

#reverse
reverse_python = lenguage[::-1]
print(reverse_python)

#Funciones
print(lenguage.capitalize())
print(lenguage.upper())
print(lenguage.count("t"))
print(lenguage.isnumeric())
print(lenguage.lower())
print(lenguage.startswith("py"))

