tareas = []
 
tareas.insert(0, {"nombre": "limpiar", "descripcion": "limpiar todo", "estado": "sin procesar"})
tareas.insert(1, {"nombre": "cocinar", "descripcion": "cocinar algo", "estado": "sin proceso"})
tareas.insert(2, {"nombre": "mantenimiento", "descripcion": "poner en punto", "estado": "sin procesar"})
tareas.insert(3, {"nombre": "tpm diario","descripcion": "limpieza y orden diario","estado": "sin procesar"})
 
def tareas_en_gestion():
  
   
  print("TAREAS A VISIALIZAR:")

  for i, tarea in enumerate(tareas):
     print((F"Tarea {i+1}: "),(f"Nombre:{tarea['nombre']} "),(f"Descripcion:{tarea['descripcion']} "),(f"Estado: {tarea['estado']}"))
       

  cambiar_tarea = input("desea realizar algun cambio en los estados de las tareas si o no?: ")
    
  if cambiar_tarea.lower() == "si":
     tarea_a_modificar = int(input("Ingrese el número de tarea que desea modificar: ")) - 1
     nuevo_estado = input("Ingrese el nuevo estado de la tarea PROCESADO O SIN PROCESAR: ")
     tareas[tarea_a_modificar]["estado"] = nuevo_estado
     print("Tareas actualizadas:")
     for i, tarea in enumerate(tareas):
        print(f"Tarea {i+1}:")
        print(f"Nombre: {tarea['nombre']}")
        print(f"Descripcion: {tarea['descripcion']}")
        print(f"Estado: {tarea['estado']}")
      
    
  else:
       print("no se modifico ninguna tarea")
     
def eliminar_tarea():
   eliminar = print(input("desea eliminar alguna tarea? si o no: "))
   if eliminar == "si":
     numero_de_tarea= print(int(input("eliga el numero de tarea a eliminar:")))-1
    
     tareas.pop[numero_de_tarea]
     print(f"tarea {numero_de_tarea} eliminada")

     for i, tarea in enumerate(tareas):
        print(F"Tarea {i+1}:")
        print(f"Nombre: {tarea['nombre']}")
        print(f"Descripcion: {tarea['descripcion']}")
        print(f"Estado: {tarea['estado']}")
   else:
       print("no se elimino ninguna tarea")

tareas_en_gestion()
eliminar_tarea()