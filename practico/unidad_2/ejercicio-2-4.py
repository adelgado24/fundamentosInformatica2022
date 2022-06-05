"""300 productos que tienen valor de 1500 dolares
Precio dolar : 110,39 peso argentino
Comision: 3%
valor sellado: 15.000"""

valor_en_pesos = 1500 * 110
comision = valor_en_pesos * 0.03
valor_con_comision = valor_en_pesos + comision
valor_total = valor_con_comision + 15000

print('El valor que se le debe cobrar al cliente es: ', int(valor_total))
print('Comision dividida: ', int(comision) / 5)
