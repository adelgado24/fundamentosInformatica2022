import sqlite3

#Trae solo los registros de los automoviles
def selectAutos():
    conexion = sqlite3.connect('Bases_de_datos/VTV_BDD.db')
    cursor = conexion.cursor()
    sentencia = "SELECT * FROM  VTV_BDD WHERE Tipo = 'Automovil'"
    cursor.execute(sentencia)
    registros = cursor.fetchall()
    for registro in registros:
        print(registro)
    conexion.close()

#Cambia el Estado del 3er vehiculo a Rechazado
def updateTercero():
    conexion = sqlite3.connect('Bases_de_datos/VTV_BDD.db')
    cursor = conexion.cursor()
    sentencia = "UPDATE VTV_BDD SET Estado = 'Rechazado' WHERE ID = 3"
    cursor.execute(sentencia)
    conexion.commit()
    conexion.close()

#Borra los registros de las motocicletas aprobadas
def deleteMotocicletas():
    conexion = sqlite3.connect('Bases_de_datos/VTV_BDD.db')
    cursor = conexion.cursor()
    sentencia = "DELETE FROM VTV_BDD WHERE Tipo = 'Motocicleta' AND Estado = 'Aprobado'"
    cursor.execute(sentencia)
    conexion.commit()
    conexion.close()

selectAutos()
updateTercero()
deleteMotocicletas()
