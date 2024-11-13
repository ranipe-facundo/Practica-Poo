from Cancion import Cancion

cancion1 = Cancion()
cancion1.set_nombre ("Un velero llamado libertad")
cancion1.set_autor ("José Luis Perales")
cancion1.set_duracion (222.0)

print(cancion1.get_nombre())
print(cancion1.get_autor())
print(cancion1.get_duracion())

####################################################################

cancion_2 = Cancion()

cancion_2.set_nombre ("La Incondicional")
cancion_2.set_autor ("Luis Miguel")
cancion_2.set_duracion (333.3)

#impresion mejorada:
print (f"Nombre de canción: {cancion_2.get_nombre()} \nNombre de autor: {cancion_2.get_autor()}\nDuración: {cancion_2.get_duracion()}")
