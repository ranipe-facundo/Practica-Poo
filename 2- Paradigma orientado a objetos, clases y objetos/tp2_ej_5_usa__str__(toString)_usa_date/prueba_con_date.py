from datetime import date
import math

fecha_1 = date(1992, 8 , 1)# Año, Mes, Día
fecha_actual = date.today()

años = (fecha_actual - fecha_1)
años = años.days/365
años = math.floor(años)

print(años)