precios = {'moto': 10, 'auto': 20, 'camioneta': 25, 'camion': 60, 'camion_acoplado':90}

def importe(categoria):
    for key, value in precios.items():
        if categoria == key:
            print(f'Vehiculo {key.upper()}, tarifa: {value}')
            break
        elif categoria == 'delorean':
            print(f'Vehiculo DELOREAN, tarifa: 200')
            break


importe('auto')
importe('delorean')