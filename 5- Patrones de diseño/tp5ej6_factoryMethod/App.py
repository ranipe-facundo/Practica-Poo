from VentaFisica import VentaFisica
from VentaDigital import VentaDigital

venta_fisica = VentaFisica()
juego1 = venta_fisica.crearVenta(60) #creo una variabley la instancio como para probar como se hace. Le paso el valor del precio base
juego1.imprimir()
# el imprimir no es algo que pide el ejercicio, pero es como una forma de ver que está devolviendo un juego fisico

print("---------------------------")
venta_digital = VentaDigital()
venta_digital.crearVenta(40,"Epic").imprimir()

#Hasta acá estaria terminado y bien el ejercicico?