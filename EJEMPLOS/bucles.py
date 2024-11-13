# continue salta a la siguiente iteracion
for i in range(5):
    if i == 2:
        continue  # Salta la iteración cuando i es igual a 2
    print(i)

# break Termina el for por completo y continua con el codigo
for i in range(5):
    if i == 2:
        break  # Termina el bucle cuando i es igual a 2
    print(i)

print("El bucle ha terminado.")
