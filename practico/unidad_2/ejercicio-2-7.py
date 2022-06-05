lista_pares = []

for n in range(101):
    if n % 2 == 0:
        lista_pares.append(n)
    else:
        pass

for par in lista_pares:
    if par != 100:
        print(par, ', ', end= "")
    else:
        print(par)