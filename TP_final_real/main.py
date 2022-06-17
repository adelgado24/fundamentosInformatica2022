from VTV import * #menu_operario,visualizar_vehiculos,aprobacion_VTV,vehiculos_API0
from vehiculos import Motocicleta, Automovil
from flask import Flask, jsonify, request
from BDD import agregar_a_BDD,vehiculos_BDD

app = Flask(__name__)

menu_operario()
visualizar_vehiculos()
aprobacion_VTV()
vehiculos_API = vehiculos_API0.copy()

agregar_a_BDD()

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
        return(jsonify({f'Vehiculos {estado}':vehiculos_estado, 'busqueda':estado, 'status':'ok'}))
    else:
        return jsonify({'vehiculos': vehiculos_BDD, 'status': 'not found'})

if __name__ == '__main__':
    app.run(debug=True,port=4000)