lista = []
tickets = []
habitacion = input('Numero de habitacion: ')
cantidad = input('Cantidad de prendas: ')
fecha = input('Fecha del servicio: ')

lista.append(habitacion)
lista.append(cantidad)
lista.append(fecha)

opciones = (1,2)

ticket = 0
eleccion = int(input('Para seleccionar el modo "Lavanderia", escriba 1, para seleccionar el modo recepcion escriba 2: '))
if eleccion in opciones and eleccion == 1:
    ticket += 1
    tickets.append(ticket)

