from Persona import Persona
from Empresa import Empresa

empleado1 = Persona(22, "f", True, True)
empleado2 = Persona(32, "f", False, True)
empleado3 = Persona(18, "m", False, True)
empleado4 = Persona(35, "m", False, True)
empleado5 = Persona(44, "f", False, True)

empresa_1 = Empresa("Standar", "Ameguino 2020")

empresa_1.aniadir_empleado(empleado1)
empresa_1.aniadir_empleado(empleado2)
empresa_1.aniadir_empleado(empleado3)
empresa_1.aniadir_empleado(empleado4)
empresa_1.aniadir_empleado(empleado5)


empresa_1.imprimir()