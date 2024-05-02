perro = True
gato = True
rata = False

resultado = perro
print("Me gustan los perros: " + str(resultado))

resultado = perro or gato
print("Me gustan los perros o gatos: " + str(resultado))

resultado = perro or gato or rata
print("Me gustan los perros o gatos o ratas: " + str(resultado))

resultado = perro and gato or rata
print("Me gustan los perros y gatos, o las ratas: " + str(resultado))

resultado = perro and not(gato)
print("Me gustan los perros y no lo gatos: " + str(resultado))

resultado = gato and not(perro) or perro and not(gato)
print("Solo me gustan los perros o solo me gustan los gatos: " + str(resultado))
