import psycopg2

conn = psycopg2.connect(
    host = 'localhost',
    database = 'tareas-app',
    user = 'postgres',
    password = 'postgres',
    port = '5432'
)
cursor = conn.cursor()

def createTask( title, description ):
    cursor.execute("INSERT INTO tareas ( titulo, descripcion ) VALUES ( %s, %s )",
        ( title , description )
    )
    conn.commit()

def editTask( id:str , title:str, description:str ):
    cursor.execute("UPDATE tareas SET titulo = %s, descripcion = %s WHERE id = %s",
        ( title , description, id )
    )
    conn.commit()

def deleteTask( id ):
    cursor.execute("DELETE FROM tareas WHERE id = %s", id)
    conn.commit()

def getAllTasks():
    cursor.execute("SELECT * FROM tareas ORDER BY id DESC")
    listado = cursor.fetchall()
    for i in range(len( listado )):
        print(f"""
        ==================
        Id: { listado[i][0] }
        Titulo: { listado[i][1] }
        Descripcion: { listado[i][2] }
        ==================
        """)    
