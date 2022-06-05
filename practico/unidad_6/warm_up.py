class Ballena:
    def __init__(self, nombre,edad,sexo,peso,mamifero):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.mamifero = mamifero
    def nadar(self):
        print(f'{self.nombre}, está nadando')
    def saltar(self):
        print(f'{self.nombre}, está saltando')
    def alimentarse(self):
        print(f'{self.nombre}, está comiendo')
    def descansar(self):
        print(f'{self.nombre}, está descansando')

    def estado(self):
        return f'El nombre de la ballena es {self.nombre},' \
              f' tiene {self.edad} años y es de genero {self.sexo}.' \
              f' Pesa {self.peso} kg y es un {"mamifero" if self.mamifero else "no mamifero"}.'


willy = Ballena('Willy', 10, 'Masculino', 2000, True)
willy_clon = Ballena('Willy', 10, 'Masculino', 2000, True)

print(willy.estado())

