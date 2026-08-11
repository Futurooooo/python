alumnos = {
    "Irving": {"carrera": "Informática", "promedio": 9.2},
    "Ana": {"carrera": "Industrial", "promedio": 8.5}
}

while True:
    print("\n---MENU---")
    print("1.Registrar alumno")
    print("2.Consultar alumno")
    print("3.Mostrar Reporte del Grupo")
    print("4.Salir")

    opcion = input("Que opcion desea realizar")

    if opcion == "1":
        nombre = input("Registre el nombre de alumno")
        carrera = input("Registre la carrera del alumno")
        promedio = float(input("Registre el promedio general del alumno"))

        alumnos[nombre]={
            "carrera": carrera,
            "promedio": promedio
        }
        print("Alumno registrado correctamente")
    elif opcion == "2":
        print("Ingrese el nombre del alumno por favor")
        if nombre in alumnos:
            carrera = alumnos[nombre]["carrera"]
            promedio = alumnos[nombre]["promedio"]

            print(f"\n---Informacion de: {nombre}---")
            print(F"carrera de {nombre}")
            print(f"promedio de {nombre}")
        else:
            print("El alumno no esta registrado")
    elif opcion =="3":
        if len (alumnos) ==0:
            print ("No hay ningun alumno registrado")
        else:
            for nombre, datos in alumnos.items():
                carrera = datos["carrera"]
                promedio = datos["promedio"]
                print(f" Nombre: {nombre} | Carrera: ${carrera} | Promedio: {promedio}")
    elif opcion == "4":
        print("Gracias por usar el gestor de alumnos")
        break
    else:
        print("Opcion No valida vuelva a intentarlo")
