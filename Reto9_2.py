while True:
    print("---MENU---")
    print("1.Agregar producto")
    print("2.Ver lista de compras")
    print("3.Vaciar lista")
    print("4.salir")

    opcion = input("Digite la opcion que desea realizar por favor: ")

    if opcion == "1":
        agregar = input("Agregue el nombre del producto: ")
        with open ("compras.txt","a")as archivo:
            archivo.write(agregar + "\n")
            print("Producto agregado")
    elif opcion == "2":
        try:
         with open("compras.txt","r")as archivo:
            contenido=archivo.read()
            print("\n----Lista completa")
            print(contenido)
        except FileNotFoundError: 
         print("El archivo no existe verifique por favor la informacion")

    elif opcion == "3":
       with open("compras.txt","w") as archivo:
           pass
       print("La lista se ha eliminado")
    elif opcion =="4":
       print("Gracias por usar el sistema que tenga buen dia")
       break
    else:
       print("Opcion no disponible vuelva a intentarlo")
