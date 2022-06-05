from pprint import pprint
from typing import Type
from datetime import date, datetime

fecha_aprobada = str(date.today().day) +"/"+ str(date.today().month) +"/"+ str(date.today().year + 1)

class Vehiculo:
    def __init__(self,ruedas, luces,frenos,gases,identificacion_vehiculo,suspension):
        self.ruedas = ruedas
        self.frenos = frenos
        self.gases = gases
        self.luces = luces
        self.identificacion_vehiculo = identificacion_vehiculo
        self.suspension = suspension

class Automovil(Vehiculo):

    def __init__(self, ruedas, luces, frenos, gases, identificacion_vehiculo, suspension,sistema_direccion,seguridad,chasis):
        super().__init__(ruedas, luces, frenos, gases, identificacion_vehiculo, suspension)
        self.sistema_direccion = sistema_direccion
        self.seguridad = seguridad
        self.chasis = chasis

    def VTV(clase):
        compra = str.split("Fecha en la que compro el auto(DD/MM/YY): ","/")
        fallas = 0
        for i in clase.__dict__.values():
            if i == "Falla":
                fallas += 1
            if fallas == 0:
                return "SIIIIIII"
            else:
                return 'Volve en unos dias campeon'

class Motocicleta(Vehiculo):

    def __init__(self, ruedas, luces, frenos, gases, identificacion_vehiculo, suspension, cubrecadena):
        super().__init__(ruedas, luces, frenos, gases, identificacion_vehiculo, suspension)
        self.cubrecadena = cubrecadena

    def VTV(clase):
        fallas = 0
        for i in clase.__dict__.values():
            if i == "Falla":
                fallas += 1
            if fallas == 0:
                return f"Tu moto esta en perfectas condiciones. La Verificación tecnica vehicular se encuentra aprobada." \
                       f"\nLa fecha de vencimiento es el {fecha_aprobada}."
            else:
                return 'Volve en unos dias campeon'



mi_auto1 = Automovil("Falla","Falla","Apto","Apto","Apto","Apto","Apto","Apto","Apto")
mi_auto2 = Automovil("Apto","Apto","Apto","Apto","Apto","Apto","Apto","Apto","Apto")
mi_moto1 = Motocicleta("Apto","Apto","Apto","Apto","Apto","Apto","Apto")

#print(mi_auto1.VTV())
#print(mi_auto2.VTV())
print(mi_moto1.VTV())
print("ejemplo github NUmero 3")
