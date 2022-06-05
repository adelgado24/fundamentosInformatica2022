recetas = [{'torta':['huevo','harina','azucar']},{'milanesa':['pan','carne']},{'ensalada':['lechuga', 'tomate', 'zanahoria']},{'brownie':['harina','chocolate']},{'pochoclos':['maiz','azucar']}]
ingredientes = []
lista = set({})

while True:
    ingrediente = input('INGREDIENTE: ')
    if ingrediente == 'quit':
        break
    else:
        ingredientes.append(ingrediente)


def validos(ingredientes):
    for i in ingredientes:
        for receta in recetas:
            for key, value in receta.items():
                if i in value:
                    lista.add(i)
    print(lista)

def recipe_recommender():
    torta = 0
    milanesa = 0
    ensalada = 0
    brownie = 0
    pochoclos = 0
    for ing in lista:
        if ing in recetas[0]['torta']:
            torta +=1
            if torta >= 2:
                print('Hacer Torta')
        if ing in recetas[1]['milanesa']:
            milanesa +=1
            if milanesa >= 2:
                print('Hacer milanesa')
        if ing in recetas[2]['ensalada']:
            ensalada +=1
            if ensalada >= 2:
                print('Hacer ensalada')
        if ing in recetas[3]['brownie']:
            brownie +=1
            if brownie >= 2:
                print('Hacer brownie')
        if ing in recetas[4]['pochoclos']:
            pochoclos +=1
            if pochoclos >= 2:
                print('Hacer Pochoclos')

validos(ingredientes)
recipe_recommender()