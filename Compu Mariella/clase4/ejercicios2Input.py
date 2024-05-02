# Ejercicio 1: Calculadora de propinas
# Pedir al usuario el monto de una cuenta de restaurante y el porcentaje
# de propina que desea dejar. Mostrar el total desglosado
# (total, propina y total a pagar incluyendo la propina)
monto = int(input("Dame el monto de tu cuenta: "))
porcentaje = int(input("Dame el porcentaje de propina: "))
propina = monto * porcentaje/100
total = monto + propina
print("El total de tu cuenta era de " + str(monto) + " , la propina que diste es " + str(propina) + " y el total es de " + str(total))

 
 
# Ejercicio 2: Conversión de monedas
# Pedir al usuario una cantidad en dólares y mostrarla convertida a euros,
# utilizando un tipo de cambio fijo. 1 USD = 0.85 EUR
dolares = int(input("Dame el dinero en dolares: "))
euros = dolares * 0.85
print("Tu cantidad de dólares en euros son " + str(euros))
 
 
# Ejercicio 3: Cálculo de IMC
# Pedir al usuario su peso en kilogramos y su altura en metros, calcular su
# Índice de Masa Corporal (IMC) y mostrarlo.
# El Índice de Masa Corporal (IMC) se calcula dividiendo el peso de una persona
# en kilogramos por el cuadrado de su altura en metros.
peso = int(input("Dame tu peso en kilogramos: "))
altura = int(input("Dame tu altura en metros: "))
altura2 = altura/100
IMC = peso / (altura2 * altura2)
print("Tu índice de masa corporal es " + str(IMC))
 
 
# Ejercicio 4: Verificador de contraseñas
# Pedir al usuario una contraseña e imprimir True si su contraseña tiene 8 o más caracteres
# o false si tiene menos.
 
contraseña = input("Dame una contraseña: ")
longitud = len(contraseña) >= 8
print(longitud)


 
# Ejercicio 5: Reemplazo de caracteres
# Pedir al usuario una palabra y luego reemplazar todas las "a" por un guion ("-") y mostrar el resultado.
palabra = input("Introduce una palabra: ")
palabraCambiada = palabra.replace('a', '-')
print(palabraCambiada)
 
# Ejericio 6: Conteo de caracteres
# Pedir al usuario una frase y contar cuántas veces aparece la letra "e" en ella (ignorando mayúsculas y minúsculas).
# Es decir, si el usuario me da la palabra Elefante, la respuesta debe ser 3.
frase = input("Dame tu frase: ")
fraseMinusculas = frase.lower()
cantidadE = fraseMinusculas.count('e')
print("La letra e aparece " + str(cantidadE) + " veces en la frase.")
 
# Ejercicio 7: Verificación de substring
# Pedir al usuario una frase y verificar si contiene la palabra "Python".
frase2 = input("Ingresa una frase: ")
contienePython = "Python" in frase2
print(contienePython)