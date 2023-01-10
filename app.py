from database import db

opcion = None
while( opcion != 0 ):
    print("""
    LISTADO DE TAREAS
    =================

    1. Crear nueva tarea
    2. Editar una tarea
    3. Ver todas las tareas
    4. Eliminar una tarea

    0. Salir
    """)

    opcion = int( input("Ingrese una opcion: ") )

    if( opcion == 1 ):
        title = input("Ingrese el titulo: ")
        description = input("Ingrese una descripcion: ")
        db.createTask( title, description )

    elif( opcion == 2 ):
        id = int(input("Ingrese el ID de la tarea a editar: "  ))
        title = input("Ingrese el nuevi titulo: ")
        description = input("Ingrese la nueva descripcion: ")
        db.editTask( id, title, description )

    elif( opcion == 3 ):
        db.getAllTasks()

    elif( opcion == 4 ):
        id = input("Ingrese el ID de la tarea a borrar")
        db.deleteTask( id )

    else:
        print("Gracias, vuelva pronto")


