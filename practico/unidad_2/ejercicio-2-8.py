precios_nuevos = []
precios = [117.12, 121.19, 128.37, 135.70, 139.47, 151.80, 157.95, 161.80,
166.20, 174.51, 179.68, 188.96, 200.89, 211.89, 225.99, 232.50,
249.12, 262.69, 177.67, 187.19, 193.81, 209.57, 216.73, 227.52,
239.24, 250.22, 256.04, 269.91, 282.93, 12.37, 92.17, 65.37,
73.26, 43.26, 78.26]

for precio in precios:
    porcentaje = precio * 0.07
    suma_porcentaje = precio + porcentaje
    precio_aumentado = round(suma_porcentaje,2)
    precios_nuevos.append(precio_aumentado)

print(precios_nuevos)