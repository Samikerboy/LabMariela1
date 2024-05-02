""" 
Ejercicio 1:
Define dos variables booleanas a y b con valores de tu elección. Imprime el resultado de las siguientes operaciones:
    a and b
    a or b
    not a 
"""
a = True
b = False
print("Ejercicio 1")
print(a and b)
print(a or b)
print(not(a))


"""
Ejercicio 2:
Define dos variables booleanas c y d con valores de tu elección. Imprime True si c es igual a d; de lo contrario, imprime False.
"""
c = True
d = False
print("Ejercicio 2")
print(c==d)


"""
Ejercicio 3:
Define tres variables enteras x, y y z con valores de tu elección. Luego, define tres variables booleanas p, q y r de la siguiente manera:
        p es True si x es mayor que y; de lo contrario, es False.
q es True si y es igual a z; de lo contrario, es False.
    r es True si x es menor o igual que z; de lo contrario, es False.
Imprime el resultado de la operación p and (q or r).
"""

x = 5
y = 7
z = 3
p = x>y
q = y==z
r = x <= z


print("Ejercicio 3")
print(p and (q or r))


""""
Ejercicio 4
Define dos variables enteras m y n con valores de tu elección. Luego, define dos variables booleanas s y t de la siguiente manera:
s es True si m es diferente de n; de lo contrario, es False.
t es True si m es mayor o igual que n; de lo contrario, es False.
Imprime el resultado de la operación (s and not t) or (not s and t).
"""
print("Ejercicio 4")
m = 4
n = 9
s = m != n
t = m >= n
print((s and not t) or (not s and t))


""""
Ejercicio 5:
Define tres variables booleanas x, y y z con valores de tu elección. Imprime el resultado de la siguiente expresión:
(x and y) or (y and z) or (x and z) 
"""
print("Ejercicio 5")
x = False
y = True
z = True
print((x and y) or (y and z) or (x and z))

""""
Ejercicio 6:
Define dos variables nombre y apellido con valores de tu elección. Concatena las dos variables para formar 
el nombre completo (en una tercera variable) e imprímelo.
"""
print("Ejercicio 6")
nombre = "Samuel"
apellido = "Garcia"
nombreCompleto = nombre + apellido
print(nombreCompleto)


""""
Ejercicio 7:
Define tres variables x, y y z con valores diferentes. 
Imprime True si x es menor que y y y es menor que z; de lo contrario, imprime False.
"""
print("Ejercicio 7")
x = 8
y = 3
z = 7
print(x > y and x > z)


""""
Ejercicio 8:
Define tres variables a, b y c con valores enteros diferentes. 
Imprime True si la suma de a y b multiplicada por c es mayor que el producto de a y c, o si b es menor que c; de lo contrario, imprime False.
"""
print("Ejercicio 8")
a = 5
b = 8
c = 7
print(((a + b) * c) > (a * c) or (b < c))
