## Clases ##


class Person:
    def __init__(self, name, surname, alias="Pelon"):
        # self.name = name
        # self.surname = surname
        self.full_name = f"{name} {surname} {alias}"

    def walk(self):
        print(f"{self.full_name} esta caminando")


my_person = Person("Ramiro", "Josafath")
print(f"{my_person.full_name}")
my_person.walk()

my_other_person = Person("Leonardo", "Leonel", "Leonidas")
print(my_other_person.full_name)
my_other_person.full_name = "Ramiro Josafath  (Pelon)"
print(my_other_person.full_name)
