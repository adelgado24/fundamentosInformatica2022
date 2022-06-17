from vehiculos import Motocicleta, Automovil
from flask import Flask, jsonify, request

vehiculos_ejemplos = []
vehiculos_API0 = []

def menu_operario():            #Cambio en el Menu simplificado
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