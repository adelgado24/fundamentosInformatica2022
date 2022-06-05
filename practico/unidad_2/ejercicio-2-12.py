estudiantes = [37128693, 38346828, 48577851, 23923908, 23747794, 46033685, 28372488, 33143443,
38122921, 38915457, 24807285, 35759559, 21061055, 33613272, 24082600, 26477319,
46655903, 46988530, 25145603, 35368988, 25393784, 21295674, 48348316, 31247247,
28498292, 37538741, 21332845, 27557703, 24435687, 38794110, 44518399, 34178717,
45788239, 36998322, 32098132, 22185788, 25030083, 21256524, 34592517, 41755997,
37570846, 30401721, 34832996, 47330519, 34380715, 42724546, 26615771, 23171192,
42223891, 40210778, 33530381, 20478110, 20753240, 28187999, 27785500, 37236996,
22981717, 27744330, 44855039, 36552090, 36824210, 39684157, 26469844, 45037525,
25916934, 41595563, 23571241, 30552911, 40100736, 36047292, 46818813, 36680587,
36107300, 41367347
]
notas = [15, 19, 19, 9, 6, 12, 20, 3, 1, 15, 10, 16, 3, 25, 18, 13, 24, 30, 7, 28, 20, 25, 28, 10, 2, 1,
18, 20, 3, 3, 19, 12, 11, 8, 24, 27, 15, 15, 19, 0, 27, 8, 29, 5, 1, 12, 8, 17, 19, 0, 0, 18, 15,
23, 22, 2, 24, 6, 10, 28, 18, 3, 15, 6, 26, 0, 21, 14, 24, 13, 10, 17, 16, 2]

dni = int(input('DNI: '))
indexado = estudiantes.index(dni)
nota = notas[indexado]

notas_avanzadas = 0
notas_intermedio_alto = 0
notas_intermedio_bajo = 0
notas_basicas = 0
notas_malas = 0

for n in notas:
    if 25 <= n <= 30:
        notas_avanzadas += 1
    elif 20 <= n <= 24:
        notas_intermedio_alto += 1
    elif 16 <= n <= 19:
        notas_intermedio_bajo += 1
    elif 10 <= n <= 15:
        notas_basicas += 1
    elif 0 <= n <= 9:
        notas_malas += 1

print('------------------------------------------------')
if dni not in estudiantes:
    print('El DNI no se encuentra en la base de datos')
elif 25 <= nota <= 30:
    print(f'Su nota es {nota}, tiene un nivel avanzado')
elif 20 <= nota <= 24:
    print(f'Su nota es {nota}, tiene un nivel intermedio alto')
elif 16 <= nota <= 19:
    print(f'Su nota es {nota}, tiene un nivel intermedio bajo')
elif 10 <= nota <= 15:
    print(f'Su nota es {nota}, tiene un nivel básico')
elif 0 <= nota <= 9:
    print(f'Su nota es {nota}, tiene un nivel por debajo del básico')
print('------------------------------------------------')
print(f'La cantidad de alumnos que se presentaron al examen es {len(estudiantes)}')
print('------------------------------------------------')
print(f'Niveles de las notas:\nNivel Avanzado: {notas_avanzadas}\nNotas Intermedias Altas: {notas_intermedio_alto}\nNotas Intermedias Bajas:{notas_intermedio_bajo}\nNotas Basicas: {notas_basicas}\nNotas por denajo del promedio: {notas_malas}')
