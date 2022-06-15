from VTV import * #menu_operario,visualizar_vehiculos,aprobacion_VTV,vehiculos_API0
from vehiculos import Motocicleta, Automovil
from flask import Flask, jsonify, request

app = Flask(__name__)

menu_operario()
visualizar_vehiculos()
aprobacion_VTV()
vehiculos_API = vehiculos_API0.copy()

#Este endpoint trae todos los vehiculos
@app.route("/vehiculos", methods =['GET'])
def vehiculosGet():
    return jsonify({"vehiculos":vehiculos_API,"status": "ok"})

#Este endpoint requiere un param, y trae un vehiculo en especifico
@app.route('/vehiculos/<NroVehiculo>', methods=['GET'])
def vehiculoGet(NroVehiculo):
    for indice, v in enumerate(vehiculos_API):
        if v['NroVehiculo'] == NroVehiculo:
            return jsonify({'NroVehiculo':vehiculos_API[indice], 'busqueda':NroVehiculo, 'status':'ok'})
    return jsonify({'vehiculos':vehiculos_API, 'status':'not found'})

#Este endpoint agrega un vehiculo
@app.route('/vehiculos', methods=['POST'])
def vehhiculoPost():
    body = request.json
    estado = body['Estado']
    nro = body['NroVehiculo']
    tipo = body['Vehiculo']
    vehiculoNuevo = {'Estado': estado, 'NroVehiculo': nro,'Vehiculo': tipo}
    vehiculos_API.append(vehiculoNuevo)
    return jsonify({'vehiculos':vehiculos_API, 'status':'ok' })

#Este endpoint modifica un vehiculo existente
@app.route('/vehiculos', methods=['PUT'])
def vehiculoPut():
    body = request.json
    estado = body['Estado']
    nro = body['NroVehiculo']
    tipo = body['Vehiculo']
    for indice, v in enumerate(vehiculos_API):
        if v['NroVehiculo'] == nro:
           v['Estado'] = estado
           v['Vehiculo'] = tipo
           return jsonify({'Vehiculo': tipo,
                           'busqueda': nro,
                           'status': 'ok'})

    return jsonify({'busqueda':vehiculos_API,
                    'status':'not found' })

#Este endpoint borra un vehiculo
@app.route('/vehiculos/<NroVehiculo>', methods=['DELETE'])
def vehiculoDelete(NroVehiculo):
    for indice, v in enumerate(vehiculos_API):
        if v['NroVehiculo'] == NroVehiculo:
            vehiculos_API[indice:indice+1] = []
            return jsonify({'Vehiculo':v, 'busqueda':NroVehiculo, 'status':'ok'})
    return jsonify({'vehiculos':vehiculos_API, 'status':'nof found' })

#Este endpoint trae los vehiculos, segun el param que le pases, (Aprobado/Rechazado)
@app.route('/aprobacion/<estado>', methods=['GET'])
def tipoGet(estado):
    vehiculos_estado = {}
    for v in vehiculos_API:
        if v['Estado'] == estado:
            vehiculos_estado[v["NroVehiculo"]] = v['Estado']
    print(vehiculos_estado)
    if len(vehiculos_estado) > 0:
        return(jsonify({f'Vehiculos {estado}':vehiculos_estado, 'busqueda':estado, 'status':'ok'}))
    else:
        return jsonify({'vehiculos': vehiculos_API, 'status': 'not found'})

if __name__ == '__main__':
    app.run(debug=True,port=4000)