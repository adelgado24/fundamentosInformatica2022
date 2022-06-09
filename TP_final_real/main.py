from vehiculos import Motocicleta, Automovil
from flask import Flask, jsonify

vehiculos_ejemplos = []
vehiculos_API0 = []

def menu_operario():
    while True:
        agregar = input("Desea agregar mas vehiculos o cerrar el sistema? agregar/salir: ")
        if agregar == "agregar" or agregar == "1":
            while True:
                tipo_vehiculo = input("¿Esta analizando un auto o moto?:")
                if tipo_vehiculo == "moto":
                    chequeo_moto()
                    break
                elif tipo_vehiculo == "auto":
                    chequeo_auto()
                    break
                else:
                    print("Ingrese bien el vehiculo")
                    break
        if agregar == "salir":
            break

def visualizar_vehiculos():
    for v in vehiculos_ejemplos:
        print("-------------------")
        print(f"Vehiculo número {vehiculos_ejemplos.index(v) + 1}")
        print("-------------------")
        print(v.VTV())
        print("")

def chequeo_moto():
    print("Ingrese 1 si esta apto, 0 si hay una falla")
    ruedas = input("Ruedas: ")
    frenos = input("Frenos: ")
    gases = input("Gases: ")
    luces = input("Luces: ")
    identificacion = input("Identificacion: ")
    suspension = input("Suspensión: ")
    cubrecadena = input("Cubrecadena: ")
    vehiculos_ejemplos.append(Motocicleta(ruedas, frenos, gases, luces, identificacion, suspension, cubrecadena))

def chequeo_auto():
    print("Ingrese 1 si esta apto, 0 si hay una falla")
    ruedas = input("Ruedas: ")
    frenos = input("Frenos: ")
    gases = input("Gases: ")
    luces = input("Luces: ")
    identificacion = input("Identificacion: ")
    suspension = input("Suspensión: ")
    sistema_direccion = input("Sistema de dirección: ")
    seguridad = input("Seguridad: ")
    chasis = input("Chasis: ")
    vehiculos_ejemplos.append(Automovil(ruedas, frenos, gases, luces, identificacion, suspension, sistema_direccion, seguridad,
                              chasis))


def aprobacion_VTV():
    for v in vehiculos_ejemplos:
        Falla = 0
        if len(list(v.__dict__.values())) == 7:
            for n in list(v.__dict__.values()):
                if n == "0":
                    Falla +=1
            if Falla == 0:
                vehiculos_API0.append(dict({"NroVehiculo" : vehiculos_ejemplos.index(v),"Estado":"Aprobado","Vehiculo":"Motocicleta"}))
            if Falla != 0:
                vehiculos_API0.append(dict({"NroVehiculo" : vehiculos_ejemplos.index(v),"Estado":"Rechazado","Vehiculo":"Motocicleta"}))
        if len(list(v.__dict__.values())) == 9:
            for n in list(v.__dict__.values()):
                if n == "0":
                    Falla +=1
            if Falla == 0:
                vehiculos_API0.append(dict({"NroVehiculo" : vehiculos_ejemplos.index(v),"Estado":"Aprobado","Vehiculo":"Automovil"}))
            if Falla != 0:
                vehiculos_API0.append(dict({"NroVehiculo" : vehiculos_ejemplos.index(v),"Estado":"Rechazado","Vehiculo":"Automovil"}))

app = Flask(__name__)

menu_operario()
visualizar_vehiculos()
aprobacion_VTV()
vehiculos_API = vehiculos_API0.copy()

@app.route("/vehiculos", methods =['GET'])
def vehiculosGet():
    return jsonify({"vehiculos":vehiculos_API,"status": "ok"})

if __name__ == '__main__':
    app.run(debug=True,port=4000)