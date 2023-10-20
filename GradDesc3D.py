import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Función a optimizar
def function_to_optimize(x, y):
    return x**2 + (3 * y)


# Derivadas parciales de la función
def gradient(x, y):
    df_dx = 2 * x
    df_dy = 3
    return np.array([df_dx, df_dy])


# Parámetros del método de gradiente descendiente
learning_rate = 0.1
num_iterations = 20

# Punto de inicio
initial_point = np.array([1.0, 1.0])

# Listas para almacenar los valores de x, y y la función en cada iteración
x_values = [initial_point[0]]
y_values = [initial_point[1]]
function_values = [function_to_optimize(initial_point[0], initial_point[1])]


# Aplicar el método de gradiente descendiente
current_point = initial_point.copy()
for i in range(num_iterations):
    gradient_value = gradient(current_point[0], current_point[1])
    print(gradient_value)
    current_point = current_point - learning_rate * gradient_value
    x_values.append(current_point[0])
    y_values.append(current_point[1])
    function_values.append(function_to_optimize(current_point[0], current_point[1]))
    print(function_values)

# Graficar la función y el recorrido del gradiente descendiente
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

x_range = np.linspace(-2, 2, 100)
y_range = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x_range, y_range)
Z = function_to_optimize(X, Y)

ax.plot_surface(X, Y, Z, cmap="viridis", alpha=0.8)
ax.scatter(x_values, y_values, function_values, color="r", marker="o")

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Valor de la función")
ax.set_title("Descenso Gradiente 3D a x^2 + 3y")

plt.show()
