#GESTOR DE TAREAS (TO DO LIST)
tareas = []

while True:
   print("\n---MENU---")
   print("1.Agregar una tarea")
   print("2.Ver todas las tareas")
   print("3.Eliminar tareas")
   print("4.Salir")
   
   respuesta = input("¿Que opcion desea realizar? (1, 2, 3, 4):")

   if respuesta == "1":
       agregar = input("Que tarea desea agregar: ")
       tareas.append(agregar)
   elif respuesta == "2":
        print(f"Hay un total de {len(tareas)} tareas en la lista.")
        if len (tareas) == 0:
            print("No hay ninguna tarea registrada")
        else:
            print("\n--- Tus Tareas Pendientes ---")
            # Usamos enumerate() para listar numerando automáticamente desde 1
            for i, tarea in enumerate(tareas, 1):
                print(f"{i}. {tarea}")
   elif respuesta == "3":
         if len (tareas) == 0:
             print("No hay tareas por eliminar")
         else:
          eliminar = input("Que tarea desea eliminar: ")
         if eliminar in tareas:
             tareas.remove(eliminar)
             print(f"Tarea {eliminar} eliminada correctamente")
         else:
             print(f"La tarea{eliminar} no se encuentra en la lista") 
   elif respuesta == "4":
        print("Gracias por usar el gestor de tareas")
        break
   else:
        print("OPCION NO VALIDA VUELVA A INTERTARLO")
       