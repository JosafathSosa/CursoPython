##     Funciones      ##


def my_function():
    print("Hola")


# my_function()


def suma_valores(x, y):
    print("El resultado es:", x + y)


suma_valores(10, 5)


def div_values(x, y):
    div = x / y
    return div


print(div_values(20, 2))


def nombre(x, y, z="Jimenez"):
    print(f"El nombre completo es: {x} {y} {z}")


x = input("Dame tu nombre")
y = input("Dame tu apellido")
nombre(x, y)


def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())


print_upper_texts("hola", "cómo", "estás")
