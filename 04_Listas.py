### Listas ###
my_list = list()
my_other_list = []

my_list = [21, 20, 30, 35, 50, 3]
print(my_list[4])
# print(len(my_list))

my_other_list = ["Ramiro", "Sosa"]

my_new_list = my_list + my_other_list
# print(my_new_list)

print(my_other_list[-2])
print(my_other_list.count("Ramiro"))

first_name, last_name = my_other_list
print(first_name)

my_other_list.append("Jimenez")#Agrega al final

my_other_list.insert(0, "Blas")#Inserta en el indice mencionado
my_other_list.remove("Sosa")#Remueve el valor mencionado
my_other_list.pop()#Elimina el ulitmo valor o valor del indice dado
my_other_list[0] = "Ramirin"

my_other_list = my_list.copy()#Copy permite copar los datos e igualarlos en este caso a otra variable
my_list.clear()#Elimina todos los datos de la lista

print(my_list)
print(my_other_list)

my_other_list.reverse()#Manda los datos en reversa
my_other_list.sort()#Ordena los datos de menor a mayor

print(my_other_list)

