import pymysql as mysql

user="root"
password="CTPI2024*"
baseDatos = "store"
host= "localhost"

miConexion = mysql.connect(host=host, user=user,  password=password, db=baseDatos)

def insertar():
    try:
        #creando un producto en una tupla
        producto = (25, "Camisa", 112.25, "ropa")
        cursor = miConexion.cursor()
        
        #texto de la consulta
        consulta = "insert into productos values(null, %s, %s, %s, %s)"
        
        #ejecutar la consulta
        resultado = cursor.execute(consulta, producto)
        
        #este es el que realiza la consulta en el servidor
        miConexion.commit()
        if (cursor.rowcount==1):
            print("Producto insertado correctamente")
        
    except miConexion.Error as error:
        print(str(error))
    




def listar():
    try:
        #crear el cursor
        cursor = miConexion.cursor()
        
        # texto de la consulta
        consulta = "select * from productos"
        cursor.execute(consulta)
        productos = cursor.fetchall()
        print(productos)
        if(len(productos)>0):
             #imprimir
            for p in productos:
                print(p)
        else:
            print("En el momento no hay productos registrados")
        
    except miConexion.Error as error:
        print(str(error))
        
        
#insertar()
listar()


