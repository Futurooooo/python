while True:
    print("\n---MENU---")
    print("1.Escriba una nota")
    print("2.Leer todas las notas")
    print("3.Borrar el diario")
    print("4.salir")

    opcion = input("Por favor escoga una de las opciones")
    if opcion == "1":
        texto_usuario = input("Por favor escriba una nota: ")
        with open("diario.txt","a") as archivo:
            archivo.write(texto_usuario + "\n")
            print("--> ¡Nota guardada correctamente!")

    elif opcion == "2":
     try:
        with open("diario.txt", "r") as archivo:
            print("Notas guardadas correctamente")
            print(contenido = archivo.read())
     except FileNotFoundError:
         print("El archivo diario no existe, favor de verificar")
     
    elif opcion == "3":
        with open ("diario.txt","w") as archivo:
            pass
        print("El diario ha sido borrado por completo")
    elif opcion == "4":
        print("Gracias por usar el menu")
        break
    else:
        print("Opcion incorecta vuelva a intetarlo por favor")
