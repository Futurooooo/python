def convertir_km_a_millas(kilometros):
    resultado = kilometros * 0.621371  
    return resultado

def calcular_precio_final(precio, porcentaje_descuento):
    monto_descuento = (precio * porcentaje_descuento) / 100
    precio_final = precio - monto_descuento  
    return precio_final

def es_multiplo_de_cinco(numero):
    if numero % 5 == 0:
        return True
    else:
        return False
    
while True:
          print("\n---MENU---")
          print("1.Convertir kilometros en millas")
          print("2.Calcular el precio final de un producto con descuento")
          print("3.Verificar si un numero es multiplo de 5")
          print("4.Salir")

          opcion = input("Digite la opcion que desea realizar: (1,2,3,4)")
          if opcion =="1":
                kilometros = float(input("Digite los kilometros que desea convertir a millas: "))
                resultado = convertir_km_a_millas(kilometros)
                print(f"Los kilometros convertidos a millas son: {kilometros}")
          elif opcion =="2":
                precio =  float(input("Digite el precio que desea saber su descuento:"))
                descuento = float(input("Digite el descuento que desea aplicar"))
                resultado = calcular_precio_final(precio,descuento)
                print(f"El precio final con {descuento} descuento es: {resultado}")
          elif opcion =="3":
                numero = int(input("Digite el numero entero que desea saber si es multiplo"))
                if es_multiplo_de_cinco(numero):
                 print("El numero es multiplo de 5") 
                else:
                 print("No es multiplo de 5")
          elif opcion == "4":
               print("Gracias por usar el sistema!!!!")
               break
          else:
               print("OPCION NO DISPONIBLE, ERROR")