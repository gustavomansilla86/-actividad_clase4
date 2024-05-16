
   

def gestionar_tareas():
    tareas = []

    # Agregar tareas
    tareas.insert(0, {"nombre": "limpiar", "descripcion": "limpiar todo", "estado": "sin procesar"})
    tareas.insert(1, {"nombre": "cocinar", "descripcion": "cocinar algo", "estado": "en proceso"})
    tareas.insert(2, {"nombre": "mantenimiento", "descripcion": "poner en punto", "estado": "sin procesar"})

    # Mostrar tareas
    print("Tareas:")
    for i, tarea in enumerate(tareas):
        print(f"Tarea {i+1}:")
        print(f"Nombre: {tarea['nombre']}")
        print(f"Descripcion: {tarea['descripcion']}")
        print(f"Estado: {tarea['estado']}")
        print()

    # Modificar estado de una tarea
    tarea_a_modificar = int(input("Ingrese el número de tarea que desea modificar (1-3): ")) - 1
    nuevo_estado = input("Ingrese el nuevo estado de la tarea: ")
    tareas[tarea_a_modificar]["estado"] = nuevo_estado

    # Mostrar tareas nuevamente
    print("Tareas actualizadas:")
    for i, tarea in enumerate(tareas):
        print(f"Tarea {i+1}:")
        print(f"Nombre: {tarea['nombre']}")
        print(f"Descripcion: {tarea['descripcion']}")
        print(f"Estado: {tarea['estado']}")
        print()

gestionar_tareas()