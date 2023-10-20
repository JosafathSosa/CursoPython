##Conditionales##

my_condi = False

if my_condi:
    print("Hola")

my_condi = 1
if my_condi == 10:
    print("Si es 10")

if my_condi > 10 and my_condi < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condi == 1:
    print("Es 1")
else:
    print("Tambien es 10")

my_string = "Hola"
if my_string:
    print(f"Mi cadena de texto no es vacia", my_string)
