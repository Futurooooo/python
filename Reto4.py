saldo = 5000

while True:
   print("\n--- MENÚ DEL CAJERO ---")
   print("1. Consultar saldo")
   print("2. Depositar dinero")
   print("3. Retirar dinero")
   print("4. Salir")
    
   respuesta = input("¿Qué opción desea realizar? (1, 2, 3, 4): ")
   
   if respuesta == "1":
    print(f"su saldo actuaL es de:{saldo}")
    
   elif respuesta == "2":
    deposito = float(input(f"Cuanto desea depositar: "))
    saldo += deposito
    print(f"su saldo actual es: {saldo}")
    
   elif respuesta =="3":
    retiro= int(input(f"Cuanto desea retirar: "))
    if retiro > saldo:
     print(f"No cuenta con suficiente Saldo para realizar dicha operacion, su saldo actual es: {saldo}")
    else:
     saldo -= retiro
     print(f"Su saldo actual es: {saldo}")
   
   elif respuesta =="4":
    print(f"Gracias por usar nuestro Banco!!!!")
    break
   else:
    print("Opcion NO VALIDA, VOLVER AL MENU PRINCIPAL")

    

     





