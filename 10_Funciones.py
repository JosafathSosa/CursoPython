##     Funciones      ##

#En C++
#int suma(int x, int y){}
#void suma(int x, string nombre){}
#double suma(int x, string nombre){}

def my_function():
    print("Hola")
my_function()


def suma_valores(x, y):
    print("El resultado es:", x + y)
suma_valores(10, 5)


def funcion_funcion():
    def hola():
        return "Hola"
    return hola()
print(funcion_funcion())


def div_values(x, y):
    div = x / y
    return div
print(div_values(20, 2))


def nombre(x, y, z="Jimenez"):
    print(f"El nombre completo es: {x} {y} {z}")
x = input("Dame tu nombre: ")
y = input("Dame tu apellido: ")
nombre(x, y)


def print_upper_texts(*texts):
    lista = []
    for text in texts:
        lista.append(text.upper()) 
    print(lista)


#so1 = input("Ingresa el primer SO ")
#so2 = input("Ingresa el segundo SO ")
#so3 = input("Ingresa el tercer SO ")

print_upper_texts("linux", "windows", "macos")
