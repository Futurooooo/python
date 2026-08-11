inventario = {
    "Laptop": {"precio": 12000, "stock": 5},
    "Mouse": {"precio": 350, "stock": 15}
}
while True:
    print("\n---MENU---")
    print("1.Registrar producto nuevo")
    print("2.Consultar producto")
    print("3.Ver inventario completo")
    print("4.Salir")

    opcion = input("¿Qué opción desea realizar? (1, 2, 3, 4): ")

    if opcion == "1":
        nombre = input("Registra el nombre del producto")
        precio = input("Registra su precio")
        stock = input("Registra la cantidad de stock disponible")
        inventario[nombre]= {
            "precio": precio,
            "stock": stock
        }
        print("Producto registrado correctamente")

    elif opcion == "2":
       nombre = input("Ingrese el nombre del producto a consultar:")
       if nombre in inventario:
          precio = inventario[nombre]["precio"]
          stock = inventario[nombre]["stock"]
    
          print(f"\n--- Información de: {nombre} ---")
          print(f"Precio: ${precio}")
          print(f"Stock disponible: {stock} piezas")
       else:
         print(f"\n[!] El producto '{nombre}' no existe en el inventario.")

    elif  opcion == "3":
     if len(inventario) == 0:
       print("El inventario está completamente vacío.")
     else:
      for producto, datos in inventario.items():
        precio = datos["precio"]
        stock = datos["stock"]
        print(f"• Producto: {producto} | Precio: ${precio} | Stock: {stock} unidades")
        
    elif opcion =="4":
          print("Gracias por usar el gestor de productos")
          break
    else:
       print("Opcion no disponible vuelva a intertarlo por favor: ")
    
  



        
    