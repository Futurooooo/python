calificacion = float(input("Ingressa tu calificacion: "))

if calificacion >= 6.0:
    print ("¡Aprobaste la materia!")
elif calificacion >= 5.0:
    print("Presenta examen extraodinario!")
else:
    print("Reprobaste la Materia :C")

    #OPERADORES LOGICOS OR/AND/NOT

    edad = 24
    inscrito = True

    if edad < 26 and inscrito == True:
       print("Tienes derecho al descuento de estudiante")