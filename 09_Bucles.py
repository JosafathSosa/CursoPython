# While
my_condition = 0
while my_condition < 20:
    print(my_condition)
    my_condition += 1
    if my_condition == 15:
        break
else:
    print("Ya no es menor que 10")

# For
numeros = ["Inicio del vec", 0, 1, 2, 3, 4, 5]
for i in numeros:
    print(i)

my_set = {"Josfath", "Sosa ", 20}
for i in my_set:
    print(i)

my_dict = {"Nombre": "Josafath", "Edad": 21, "Lenguajes": {"Swift", "Python"}, 1: 1.77}
for i in my_dict:
    if i == "Nombre":
        print(i)
        break
