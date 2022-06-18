from VTV import * #menu_operario,visualizar_vehiculos,aprobacion_VTV,vehiculos_API0
from flask import Flask, jsonify, request
from persistencia_pickles import agregar_a_BDD,vehiculos_BDD, to_csv
import sqlite3

app = Flask(__name__)

#Menu y nuevos registros
menu_operario()
visualizar_vehiculos()
aprobacion_VTV()
vehiculos_API = vehiculos_API0.copy()

#Actualizacion de las BDD
agregar_a_BDD()
to_csv()

#API
#Este endpoint trae todos los vehiculos
@app.route("/vehiculos", methods =['GET'])
def vehiculosGet():
    return jsonify({"vehiculos":vehiculos_BDD,"status": "ok"})

#Este endpoint requiere un param, y trae un vehiculo en especifico
@app.route('/vehiculos/<ID_del_Vehiculo>', methods=['GET'])
def vehiculoGet(ID_del_Vehiculo):
    for indice, v in enumerate(vehiculos_BDD):
        if v['ID del Vehiculo'] == int(ID_del_Vehiculo):
            return jsonify({'Vehiculo encontrado':vehiculos_BDD[indice], 'busqueda':ID_del_Vehiculo, 'status':'ok'})
    return jsonify({'vehiculos':vehiculos_BDD, 'status':'not found'})

#Este endpoint agrega un vehiculo, El ID del Vehiculo hay que pasarlo como str en postman
@app.route('/vehiculos', methods=['POST'])
def vehhiculoPost():
    body = request.json
    estado = body['Estado']
    nro = body['ID del Vehiculo']
    tipo = body['Tipo']
    fecha = body['Fecha']
    vehiculoNuevo = {'Estado': estado, 'ID del Vehiculo': int(nro),'Tipo': tipo,'Fecha': fecha}
    vehiculos_BDD.append(vehiculoNuevo)
    return jsonify({'vehiculos':vehiculos_BDD, 'status':'ok' })

#Este endpoint modifica un vehiculo existente, El ID del Vehiculo hay que pasarlo como str en postman
@app.route('/vehiculos', methods=['PUT'])
def vehiculoPut():
    body = request.json
    estado = body['Estado']
    nro = body['ID del Vehiculo']
    tipo = body['Tipo']
    fecha = body['Fecha']
    for indice, v in enumerate(vehiculos_BDD):
        if v['ID del Vehiculo'] == int(nro):
           v['Estado'] = estado
           v['Tipo'] = tipo
           v['Fecha'] = fecha
           return jsonify({'ID de vehiculo modificado': nro,
                           'status': 'ok'})

    return jsonify({'busqueda':vehiculos_BDD,
                    'status':'not found' })

#Este endpoint borra un vehiculo
@app.route('/vehiculos/<ID_del_Vehiculo>', methods=['DELETE'])
def vehiculoDelete(ID_del_Vehiculo):
    for indice, v in enumerate(vehiculos_BDD):
        if v['ID del Vehiculo'] == int(ID_del_Vehiculo):
            vehiculos_BDD[indice:indice+1] = []
            del vehiculos_BDD[int(ID_del_Vehiculo) + 1]
            return jsonify({'Vehiculo':v, 'busqueda':ID_del_Vehiculo, 'status':'ok'})
    return jsonify({'vehiculos':vehiculos_BDD, 'status':'not found' })

#Este endpoint trae los vehiculos, segun el param que le pases, (Aprobado/Rechazado)
@app.route('/aprobacion/<estado>', methods=['GET'])
def tipoGet(estado):
    vehiculos_estado = {}
    for v in vehiculos_BDD:
        if v['Estado'] == estado:
            vehiculos_estado[v["ID del Vehiculo"]] = v['Estado']
    if len(vehiculos_estado) > 0:
        return jsonify({f'Vehiculos {estado}':vehiculos_estado, 'busqueda':estado, 'status':'ok'})
    else:
        return jsonify({'vehiculos': vehiculos_BDD, 'status': 'not found'})

@app.route('/incidentes', methods=['GET'])
def incidentesGet():
    return jsonify({'Cantidad de incidentes':cantidad_incidentes,'status':'ok'})

#SQL

lista_para_BDD = []

#Convierte los valores de vehiculos_BDD a tuplas para poder insertarlos a la BDD
def a_tupla():
    for i in vehiculos_BDD:
        lista_para_BDD.append(tuple(i.values()))

#Creacion de la base de datos y tabla
def create_DB():
    conexion = sqlite3.connect("Bases_de_datos/VTV_BDD.db")
    conexion.commit()
    conexion.close()

def create_table():
    conexion = sqlite3.connect("Bases_de_datos/VTV_BDD.db")
    cursor = conexion.cursor()
    sentencia = """
                CREATE TABLE VTV_BDD (
                ID INTEGER,
                Fecha TEXT,
                Estado TEXT,
                Tipo TEXT)
                """
    cursor.execute(sentencia)
    conexion.commit()
    conexion.close()

#Estas dos funciones actualizan los datos de la tabla
def delete_data():
    conexion = sqlite3.connect("Bases_de_datos/VTV_BDD.db")
    cursor = conexion.cursor()
    sentencia = "DELETE FROM VTV_BDD"
    cursor.execute(sentencia)
    conexion.commit()
    conexion.close()

def add_data():
    conexion = sqlite3.connect("Bases_de_datos/VTV_BDD.db")
    cursor = conexion.cursor()
    sentencia = "INSERT INTO VTV_BDD VALUES (?,?,?,?)"
    cursor.executemany(sentencia,lista_para_BDD)
    conexion.commit()
    conexion.close()

a_tupla()
#create_DB()
#create_table()
delete_data()
add_data()

if __name__ == '__main__':
    app.run(debug=True,port=4000)