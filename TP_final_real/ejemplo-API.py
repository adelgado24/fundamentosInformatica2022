from flask import Flask, jsonify, request

app = Flask(__name__)

productos = [
    {'Nombre': 'tensiometro', 'stock': 5},
    {'Nombre': 'termometro', 'stock': 20},
    {'Nombre': 'ibupofreno', 'stock': 500},
    {'Nombre': 'paracetamol', 'stock': 450},
]
@app.route('/productos', methods = ["GET"])
def getProductos():
    return jsonify({'productos': productos,'status':'ok'})

@app.route('/productos/<producto>', methods = ["GET"])
def getProducto(producto):
    for indice,p in enumerate(productos):
        if p['Nombre'] == producto:
            return jsonify({'producto': productos[indice], 'busqueda': producto, 'status': 'ok'})
    return jsonify({'productos': productos, 'status': 'nof found'})

@app.route('/productos', methods=['POST'])
def productoPost():
    body = request.json
    nombre = body['nombre']
    stock  = body['stock']
    productoAlta = {'Nombre': nombre, 'stock': stock}
    return jsonify({'productos':productoAlta, 'status':'ok' })

@app.route('/productos', methods=['PUT'])
def productoPut():
    body = request.json
    nombre = body['nombre']
    stock  = body['stock']
    for indice, p in enumerate(productos):
        if p['Nombre'] == nombre:
           p['stock'] = stock
           return jsonify({'producto': p,
                           'busqueda': nombre,
                           'status': 'ok'})

    return jsonify({'busqueda':productos,
                    'status':'not found' })

if __name__ == '__main__':
    app.run(debug = True, port = 4000)

