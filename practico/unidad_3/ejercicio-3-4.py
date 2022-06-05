encuesta = {'anonimo1': '6', 'anonimo2': '9', 'anonimo3': '5', 'anonimo4':
'x', 'anonimo5': 'x', 'anonimo6': '8', 'anonimo7': '3',
'anonimo8': '10', 'anonimo9': '4', 'anonimo10': '5', 'anonimo11':
'x', 'anonimo12': '2', 'anonimo13': '7', 'anonimo14': '5',
'anonimo15': '2', 'anonimo16': '8', 'anonimo17': '10'}

#a) Contar y remover
print('\n--- Ejercicio a ---')
valores = list(encuesta.values())
x = valores.count('x')
print(f'La cantidad de empleados que no respondieron son: {x}')

#No se puede modificar un dic mientras se itera, por lo que se tiene que copiar
copia_encuesta = encuesta.copy()
for k in copia_encuesta:
    if encuesta[k] == 'x':
        encuesta.pop(k)

print(encuesta)

#b) print cuantos respondieron
print('\n--- Ejercicio b ---')
print(f'La cantidad de personas que sí respondieron la encuesta son: {len(encuesta)}')

#c) suma y porcentaje
print('\n--- Ejercicio c ---')

suma = 0
for i in encuesta.values():
    suma += int(i)
print(f'La cantidad de valores sumados es de {suma}')

porcentaje_aprobados = (suma / ((len(encuesta.values())) * 10)) * 100
print(f'El porcentaje es de {round(porcentaje_aprobados)}%')

#d) Nros
print('--- Ejercicio d ---')
nros = set(encuesta.values())

ordenada = []
for nro in nros:
    ordenada.append(int(nro))
print(sorted(ordenada))

