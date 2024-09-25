## Clases ##
#Pilares de la programación orientada a objetos

#Abstracción: Permite crear clases y objetos que representan entidades del mundo real o conceptos abstractos.

#Encapsulamiento: Restringe el acceso directo a los atributos y métodos de un objeto, permitiendo su manipulación solo a través de métodos públicos (getters y setters). 

#Herencia: Es el mecanismo por el cual una clase (subclase) puede heredar atributos y métodos de otra clase (superclase). Facilita la reutilización del código y permite crear jerarquías de clases.

#Polimorfismo: Permite que los objetos de diferentes clases se comporten de manera distinta al compartir la misma interfaz. 
# Un gato hace miau y un perro guau


#El constructor te permite asignar valores a los atributos de la clase en el momento en que se crea el objeto. Esto evita tener que asignar estos valores manualmente después de la creación del objeto.
class Person:
    def __init__(self, name, lastName, peliculasFavoritas, alias="Pelon"):
        self.name = name
        self.lastName = lastName
        self.full_name = f"{name} {lastName} {alias}"
        self.peliculasFavoritas = peliculasFavoritas

    def walk(self):
        print(f"{self.full_name} esta caminando")
    
    def peliculas(self):
        for pelicula in self.peliculasFavoritas:
            print(pelicula)


peliculasFavoritas = ["Interestelar" , "Climax", "Saw"]

#Se crea un instancia u objeto de la clase Person
my_person = Person("Josafath", "Sosa", peliculasFavoritas)



print(f"Soy {my_person.full_name} y mis peliculas favoritas son", ", ".join(my_person.peliculasFavoritas))
my_person.walk()
my_person.peliculas()
print(my_person.name)


#Se crea otra instancia u objeto de la clase persona
my_other_person = Person("Leonardo", "Leonel", "Leonidas")
print(my_other_person.full_name)
my_other_person.full_name = "Jose Juan Peralta"
print(my_other_person.full_name)

#https://www.hackerrank.com/
