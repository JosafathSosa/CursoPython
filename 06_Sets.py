# SETS #
my_set = set()
my_other_set = {}

# print(type(my_set))
# print(type(my_other_set)) Inicialmente es un diccionario

my_set = {"JavaScript"}
my_other_set = {"Josafath", "Sosa", 21}
print(type(my_other_set))

my_other_set.add("Jimenez")  # Es una estructura no ordenada, no admite repetidos
print(my_other_set)

print("Sosa" in my_other_set)

my_other_set.remove(21)
print(my_other_set)

# my_other_set.clear()

my_new_set = my_other_set.union(my_set)
print(my_new_set)

# del my_other_set //elimina toda la propiedad
