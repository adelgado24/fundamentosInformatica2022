from vehiculos import Motocicleta, Automovil
import requests

vehiculos_ejemplos = []
vehiculos_API0 = []

def menu_operario():
    while True:
        opcion = input("Bienvenido! eljia una opcion para continuar\n1.Agregar un auto\n2.Agregar una moto\n3.Salir\nOpcion: ")
        if opcion == "1":
            chequeo_auto()
        elif opcion == "2":
            chequeo_moto()
        elif opcion == "3":
            break
        else:
            print("Elija una opcion valida")


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
                vehiculos_API0.append(dict({"ID del Vehiculo" : str(vehiculos_ejemplos.index(v) + 1),"Estado":"Aprobado","Tipo":"Motocicleta"}))
            if Falla != 0:
                vehiculos_API0.append(dict({"ID del Vehiculo" : str(vehiculos_ejemplos.index(v) + 1),"Estado":"Rechazado","Tipo":"Motocicleta"}))
        if len(list(v.__dict__.values())) == 9:
            for n in list(v.__dict__.values()):
                if n == "0":
                    Falla +=1
            if Falla == 0:
                vehiculos_API0.append(dict({"ID del Vehiculo" : str(vehiculos_ejemplos.index(v) + 1),"Estado":"Aprobado","Tipo":"Automovil"}))
            if Falla != 0:
                vehiculos_API0.append(dict({"ID del Vehiculo" : str(vehiculos_ejemplos.index(v) + 1),"Estado":"Rechazado","Tipo":"Automovil"}))

#API de 3eros, INCIDENTES VIALES
#Este request trae datos sobre todos los cortes generados en capital generados por incidentes viales. A modo de ejemplo traimos datos del mes de diciembre de 2020.
url_incidentes = "https://apitransporte.buenosaires.gob.ar/transito/v1/eventos?month=2020-12&provider=769&client_id=8de4a6411cf04d72a34b3f06f60002c9&client_secret=37fE78571E804261aac6a7834F1Ae64f"

response = requests.get(url_incidentes)
status_code = response.status_code
cantidad_incidentes = 0

if status_code == 200:
    json = response.json()['list']
    for i in json:
        if i['type'] != "Manifestación": #De esta manera sacamos los cortes generados por manifestaciones porque no nos sirven como dato para el analisis que queremos realizar
            cantidad_incidentes += 1
        else:
            cantidad_incidentes += 0
else:
    print("Error en la solicitudo de la API de incidentes")