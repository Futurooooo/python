nombre = input("Ingrese su nombre por favor: ")
promedio = float(input("Ingrese su promedio final del semestre: "))
ingreso = float(input("Ingrese su ingreso mensual total: "))

if promedio >= 9.5:
    print(f"Felicidades{nombre} tienes Beca de EXCELENCIA")
elif promedio >=8.5 and ingreso < 12000:
    print(f"Felicidades {nombre} tienes derecho a Beca Academica y social")
elif promedio >=7.0:
    print (f"Felicidades {nombre} tienes derecho a una Beca Parcial")
else:
    print("Lo lamento no tienes derecho a una Beca")
