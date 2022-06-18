import sqlite3
#from main import vehiculos_BDD

ejemplo = [{'ID del Vehiculo': 1, 'Fecha': '15/06/2022', 'Estado': 'Aprobado', 'Tipo': 'Motocicleta'},
{'ID del Vehiculo': 2, 'Fecha': '15/06/2022', 'Estado': 'Aprobado', 'Tipo': 'Motocicleta'},
{'ID del Vehiculo': 3, 'Fecha': '15/06/2022', 'Estado': 'Aprobado', 'Tipo': 'Automovil'}]

lista_t = []
for i in ejemplo:
    lista_t.append(tuple(i.values()))

lista_f = [(8,"sdfs","aefas","aesdfsd"),(9,"sdfs","aefas","aesdfsd")]


def create_DB():
    conexion = sqlite3.connect("VTV_BDD.db")
    conexion.commit()
    conexion.close()

def create_table():
    conexion = sqlite3.connect("VTV_BDD.db")
    cursor = conexion.cursor()
    sentencia = """
                CREATE TABLE VTV_BDD (
                ID INTEGER,
                Fecha TEXT,
                Tipo TEXT,
                Estado TEXT)
                """
    cursor.execute(sentencia)
    conexion.commit()
    conexion.close()

def add_data():
    conexion = sqlite3.connect("VTV_BDD.db")
    cursor = conexion.cursor()
    sentencia = "INSERT INTO VTV_BDD VALUES (?,?,?,?)"
    cursor.executemany(sentencia,lista_f)
    conexion.commit()
    conexion.close()

if __name__ == '__main__':
    create_DB()
    create_table()
    add_data()
