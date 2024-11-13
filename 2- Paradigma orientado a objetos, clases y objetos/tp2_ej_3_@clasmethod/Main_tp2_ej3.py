from Alumno import Alumno

#instancia normal, que usa el __init__

alumno = Alumno("Facundo","Rañipe",36727511) # Solicita los 3 argumentos

print(f'Usando el constructor __init__ : {alumno.getNombreYapellido()}{" - DNI: "}{alumno.getDni()}')

#instancia de @clasmethod Alumno, tiene el mismo nombre pero puedo crear una instancia sin argumentos porque el constructor ya los inicializa en campos vacios y dni en 0
alumno1 = Alumno.Alumno()

print(f'Creado con @clasmethod Alumno: {alumno1.getNombreYapellido()}{" - DNI: "}{alumno1.getDni()}') #imprime con lo definido por el constructor, campos vacios y dni en 0

#Usando @Clasmethod '.iniciar_con_nom_ape' necesito darle los argumentos de 'nombre' y 'apellido' dni queda en 0 como esta inicializado en el constructor

alumno2 = Alumno.iniciar_con_nom_ape("Martin","Rosales")

print(f'Usando @Clasmethod .iniciar_con_nom_ape: {alumno2.getNombreYapellido()}{" - DNI: "}{alumno2.getDni()}')

# Instancia de Alumno con el @clasmethod que es igual a clasmethod Alumno sin argumenots, solo cambia el nombre. No solicita argumentos

alumno3 = Alumno.iniciar()

print(f'Usando el @clasmethod .iniciar {alumno1.getNombreYapellido()}{" - DNI: "}{alumno1.getDni()}')