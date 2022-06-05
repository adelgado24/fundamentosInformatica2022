shopping_cart = []

def comprar():
    print(shopping_cart)

while True:
    item = input('Ingrese el producto que desea agregar al carrito: ')
    shopping_cart.append(item)
    resp = input('¿Desea comprar lo que se encuentra en el carrito o seguir agregando productos? comprar/ continuar: ')
    if resp == 'comprar':
        comprar()
    else:
        continue

