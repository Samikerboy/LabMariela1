import math

# Ejercicio 1
# Pedirle al usuario su año de nacimiento y darle su edad
año = int(input("Dame tu año de nacimiento: "))
print("Tienes " + str((2024 - año)) + " años de edad.")

# Ejercicio 2
# Pedirle al usuario su nombre y apellido (en variables diferentes)
# concatenarlas, y decirle cuántos caracteres tiene.
nombre = input("Dame tu nombre: ")
apellido = input("Dame tu apellido: ")
nombreCompleto = nombre + apellido
print(len(nombreCompleto))

# Ejercicio 3
# Pedir al usuario el radio de un círculo y mostrar el área y el perímetro.
radio = int(input("Dame el radio del círculo: "))
area = str(math.pi * radio//2)
perimetro = str(2 * math.pi * radio)
print(" El área de tu círculo es " + area + " y el perímetro es " + perimetro)

# Ejercicio 4
# Conversión de temperatura: Pedir al usuario una temperatura en grados Celcius y mostrarla convertida en Fahrenheit.
celcius = int(input("Dame la temperatura en celcius: "))
fahrenheit = (1.8 * celcius) + 32
print("Los grados celcius en fahrenheit son " + str(fahrenheit))

# Ejercicio 5
# Cálculo de descuento: Pedir al usuario el precio de un producto y un porcentaje de descuento, calcular el precio final y mostrarlo.
precio = int(input("Dame el precio del producto: "))
porcentaje = int(input("Dame el porcentaje de descuento: "))
descuento = precio / porcentaje
total = precio - descuento
print("El total de tu producto es " + str(total))

