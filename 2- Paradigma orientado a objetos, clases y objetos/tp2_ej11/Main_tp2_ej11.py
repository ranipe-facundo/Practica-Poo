from Empresa import Empresa
from Persona import Persona

empleado_1 = Persona("Facundo Rañipe", 50, 'M', False, True)
empleado_2 = Persona("Hernan Gutierrez", 48, 'F', False, True)
empleado_3 = Persona("Emiliano Martinez", 20, 'M', True, False)
empleado_4 = Persona("Juan Jimenez", 25, 'F', True, False)
empleado_5 = Persona("Ezequiel Ricardo", 22, 'F', True, False)

empresa_1 = Empresa("YPF", "Rivadavia 123")

empresa_1.agregar_empleado(empleado_1)
empresa_1.agregar_empleado(empleado_2)
empresa_1.agregar_empleado(empleado_3)
empresa_1.agregar_empleado(empleado_4)
empresa_1.agregar_empleado(empleado_5)

print(f"Cantidad de empleados: {empresa_1.cantidad_empleados()}")
empresa_1.imprime_empleados()