from figuras import Esfera, Cubo, prismaRectangular


def user_menu():

    print('Que figura imprimir'
          '\n1 - Esfera'
          '\n2 - Cubo'
          '\n3 - Rectangulo')

    option = input('>> ')

    if option == "1":
        radio = input('Radio en CM >> ')
        esfera = Esfera(radio)
        return esfera.get_radio()



print(user_menu())
