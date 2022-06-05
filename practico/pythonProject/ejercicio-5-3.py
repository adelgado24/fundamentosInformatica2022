notas = [{'ID':123, 'parcial_1': 7,'parcial_2': 4,'final': 5,'concepto': 3},{'ID':124, 'parcial_1': 3,'parcial_2': 2,'final': 10}]
promedios = []

def promedio(ID):
    for i in notas:
        if ID in i.values():
            try:
                suma1 = i['parcial_1'] + i['parcial_2'] + i['final'] + i['concepto']
                promedio1 = suma1 /4
                promedios.append(dict(ID= ID,promedio=promedio1))
                print(promedio1)
            except:
                suma2 = i['parcial_1'] + i['parcial_2'] + i['final']
                promedio2 = suma2 / 3
                promedios.append(dict(ID = ID,promedio=promedio2))
                print(promedio2)
    print(promedios)

promedio(124)
promedio(123)

