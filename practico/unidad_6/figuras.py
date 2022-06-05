class Esfera:
    def __init__(self, radio):
        self.nombre = 'esfera'
        self.radio = radio

    def get_name(self):
        return f'La figura es una {self.nombre}'

    def get_radio(self):
        return f'El radio de la figura es de {self.radio} cm'


class Cubo:
    def __init__(self, lado):
        self.nombre = 'cubo'
        self.lado = lado


class prismaRectangular:
    def __init__(self, base, altura, profundidad):
        self.nombre = 'rectangulo'
        self.base = base
        self.altura = altura

esfera = Esfera(5)
#print(esfera.get_radio())
