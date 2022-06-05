animals_lista = ['perro', 'gato', 'raton']
animals_tupla = ('perro', 'gato', 'raton')
animals_conjunto = {'perro', 'gato', 'raton'}
animals_diccionario = {'animal1':'perro','animal2': 'gato','animal3': 'raton'}

types = [animals_lista, animals_tupla, animals_conjunto, animals_diccionario]
#a) Prints
print('--- Ejercicio a ---')
for t in types:
    print(t)

#b) Types
print('\n--- Ejercicio b ---')
for t in types:
    print(type(t))

#c) Agregar items
print('\n--- Ejercicio c ---')
#Lista
animals_lista.append('python')
print(animals_lista)
#Tupla
a = list(animals_tupla)
a.append('Python')
animals_tupla = tuple(a)
print(animals_tupla)
#Conjunto/Set
animals_conjunto.add('Python')
print(animals_conjunto)
#Diccionario
animals_diccionario['animal4'] = 'Python'
print(animals_diccionario)

#d)No se admiten valores repetidos en los sets
animals_conjunto.add('Python')
print(animals_conjunto)

