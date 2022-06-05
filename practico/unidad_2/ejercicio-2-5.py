nombres = ["ernest" , "martin andrés" , "sofia" , "lucia" , "jose maría" , "abril"]

print('Lista 1: ' ,end = "")
for nombre in nombres:
    print(nombre + '; ', end = "")

print("\n")
nombres_nuevos = nombres + ["martina", "josefina isables", "tomas"]

print('Lista 2: ' ,end = "")
for nombre in nombres_nuevos:
    print(nombre + '; ', end = "")

print('\n')
print(nombres_nuevos[:-1])