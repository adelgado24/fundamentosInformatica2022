from main import *
import json, pickle
from datetime import date

vehiculos_BDD = []

def agregar_a_BDD():
    vehiculos_API = vehiculos_API0.copy()
    hoy = date.today()
    cantidad_vehiculos = []

    load_file = open('test.pkl', 'rb')
    while True:
        try:
            vehiculo_file = pickle.load(load_file)
            cantidad_vehiculos.append(vehiculo_file)
        except EOFError:
            break
    load_file.close()

    store_file = open(r'test.pkl', 'ab')
    for v in vehiculos_API:
        pickle.dump({"ID del Vehiculo": int(v['ID del Vehiculo']) + len(cantidad_vehiculos),"Fecha":hoy.strftime("%d/%m/%Y"),"Estado":v['Estado'],"Tipo":v['Tipo']}, store_file)
    store_file.close()

    see_file = open('test.pkl', 'rb')
    while True:
        try:
            vehiculo_file = pickle.load(see_file)
            vehiculos_BDD.append(vehiculo_file)
            print(vehiculo_file)
        except EOFError:
            break
    see_file.close()

    load_file.close()

