import random


# Escribe un programa que determine si un número es par o impar. 
# Crea una funcion, pasale un numero y determina si el numero es par o impar
# Un número se considera par cuando es divisible por 2, es decir, cuando al dividirlo entre 2 el resto es 0. 
# Recuerda el operador aritmetico que podria ayudar a saber el residuo
def par_o_impar(numero):
    if numero % 2 == 0:
        print(f"{numero} es par")
    else:
        print(f"{numero} es impar")


# Prueba con diferentes números
par_o_impar(7)  # Salida: 7 es impar
par_o_impar(4)  # Salida: 4 es par

# Escribe un programa que cuente cuántas vocales hay en una palabra. Declara una funcion y pasale un string
# Declara una variable string con las vocales en min y may
# Itera el string y pregunta si la posicion actual es vocal y suma 1 en un contado.
# Puedes usar la palabra reservada in para verificar si dicha posicion es una vocal
# Imprime al final la cantidad de vocales encontradas y la palabra 

def contar_vocales(palabra):
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in palabra:
        if letra in vocales:
            contador += 1
    print(f"Hay {contador} vocales en '{palabra}'")

# Prueba
contar_vocales("Python")  # Salida: Hay 1 vocales en 'Python'


def adivina_numero():
    numero_secreto = random.randint(1, 10)
    intento = None
    while intento != numero_secreto:
        intento = int(input("Adivina el número (entre 1 y 10): "))
        if intento < numero_secreto:
            print("Muy bajo!")
        elif intento > numero_secreto:
            print("Muy alto!")
    print("¡Correcto!")


# Prueba
adivina_numero()


def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True


# Prueba
print(es_primo(11))  # Salida: True
print(es_primo(4))  # Salida: False


def invertir_cadena(cadena):
    print(cadena[::-1])


# Prueba
invertir_cadena("Hola")  # Salida: aloH
