from datetime import date

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

    def VTV(self):
        fallas = 0
        for i in self.__dict__.values():
            if i == "0":
                fallas += 1
        if fallas == 0:
            return f"Tu automovil está en perfectas condiciones. La Verificación tecnica vehicular se encuentra aprobada." \
                    f"\nLa fecha de vencimiento es el {fecha_aprobada}."
        else:
            return 'Su automovil no cumple con las condiciones para el aprobado de la VTV. Regrese en un mes.'

class Motocicleta(Vehiculo):

    def __init__(self, ruedas, luces, frenos, gases, identificacion_vehiculo, suspension, cubrecadena):
        super().__init__(ruedas, luces, frenos, gases, identificacion_vehiculo, suspension)
        self.cubrecadena = cubrecadena

    def VTV(self):
        fallas = 0
        for i in self.__dict__.values():
            if i == "0":
                fallas += 1
        if fallas == 0:
            return f"Tu moto esta en perfectas condiciones. La Verificación tecnica vehicular se encuentra aprobada." \
                    f"\nLa fecha de vencimiento es el {fecha_aprobada}."
        else:
            return 'Su motocicleta no cumple con las condiciones para el aprobado de la VTV. Regrese en un mes.'






