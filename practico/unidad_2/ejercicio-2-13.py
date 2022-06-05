deudas = [1323.23, 5755.20, 1928, 3876, 4539, 4648, 4000, 3713, 3148, 1240, 3232, 4948, 2491,
2092, 3471, 1704.92, 4630, 4697, 1495.30, 2174, 2897, 2505, 3502, 2573]
deudas_con_intereses = []

i = 0
while i < len(deudas):
    porcentaje = deudas[i] * 0.035
    nueva_deuda = deudas[i] + porcentaje
    deudas_con_intereses.append(nueva_deuda)
    i += 1
else:
    print(deudas_con_intereses)