from main import *
import json, pickle
from datetime import date
import csv

vehiculos_BDD = []

def agregar_a_BDD():
    vehiculos_API = vehiculos_API0.copy()
    hoy = date.today()
    cantidad_vehiculos = []
    #Este primer paso sirve para ver cuantos registros de vehiculos ya hay
    load_file = open('Bases_de_datos/test.pkl', 'rb')
    while True:
        try:
            vehiculo_file = pickle.load(load_file)
            cantidad_vehiculos.append(vehiculo_file)
        except EOFError:
            break
    load_file.close()

    #En este paso se agregan los nuevos vehiculos, pero a partir de la ultima ID que ya existia
    store_file = open(r'Bases_de_datos/test.pkl', 'ab')
    for v in vehiculos_API:
        pickle.dump({"ID del Vehiculo": int(v['ID del Vehiculo']) + len(cantidad_vehiculos),"Fecha":hoy.strftime("%d/%m/%Y"),"Estado":v['Estado'],"Tipo":v['Tipo']}, store_file)
    store_file.close()

    #En este ultimo paso se almacenan en la lista vehiculos_BDD todos los vehiculos que alguna vez se registraron y no solo los de la ultima vez que se corrió el programa
    see_file = open('Bases_de_datos/test.pkl', 'rb')
    while True:
        try:
            vehiculo_file = pickle.load(see_file)
            vehiculos_BDD.append(vehiculo_file)
            print(vehiculo_file)
        except EOFError:
            break
    see_file.close()

    load_file.close()

#Esta funcion pasa los datos a un archivos csv
def to_csv():
    keys = vehiculos_BDD[0].keys()
    with open('Bases_de_datos/registros_csv.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(vehiculos_BDD)

