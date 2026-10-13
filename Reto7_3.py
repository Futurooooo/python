def calcular_propina(total_cuenta, porcentaje_propina):
    monto_propina = (total_cuenta * porcentaje_propina)/100
    precio_final = total_cuenta+monto_propina
    return precio_final

def clasificar_temperatura(grado):
    if grado <=15:
         print("Hace frio")
    elif grado <=28:
         print("Clima agradable")
    else:
         print("Hace calor!!!!!")
         return resultado_clima

def es_par_y_positivo(numero):
     if numero > 0 and numero % 2 == 0:
            return True
     else:
            return False

while True:
        print("\n---MENU---")
        print("1.Calcular propina")
        print("2.Clasificar temperatura")
        print("3.Numero es par y positivo")
        print("4.Salir")
        
        opcion = input("Digite la opcion que desea realizar: (1,2,3,4)")

        if opcion == "1":
            total_cuenta = float((input("Digite el costo de la cuenta: ")))
            porcentaje = float(input("Digite el porcentaje de propina: "))

            precio_final = calcular_propina(total_cuenta,porcentaje)
            print(f"La cuenta final con propina es: {precio_final}")

        elif opcion == "2":
              grado = float(input("Digite la cantidad de grados celsius"))
              resultado_clima = clasificar_temperatura(grado)
              print(f"Diagnostico de clima {resultado_clima}")
              
        elif opcion == "3":
             numero = int(input("Digite el numero que desea saber si es par y positivo"))
             if es_par_y_positivo(numero):
                print("El numero es par y positivo")
             else:
                print("El numero no es par")

        elif opcion == "4":
              print("Gracias por usar el sistema!!!!")
              break
        else:  
             print("OPCION NO DISPONIBLE, ERROR")

