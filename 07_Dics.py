my_dict = dict()
my_other_dict = {}

my_other_dict = {"Nombre": "Josafath", "Edad": 21}
my_dict = {"Nombre": "Josafath", "Edad": 21, "Lenguajes": {"Swift", "Python"}, 1: 1.77}


my_dict["Nombre"] = "Ramiro Josafath"

# print(my_dict["Nombre"])

# my_dict["Mi otra edad"] = 1.68
# print(my_dict[3])

# del my_dict["Lenguajes"]
# print(my_dict)

# print(1 in my_dict)

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)
