usuarios = ["marmeant", "gruntmar", "tokcie", "ciebank", "mueslicie", "sanero", "robedrock", "admin", "derivero","posloth", "claypo", "locustpo", "mostter"]
username = input('Inserte su username: ')

if username in usuarios and username == 'admin':
    print(f'Bienvenido Administrador, en que lo puedo ayudar')
elif username in usuarios:
    print(f'Bienvenido estimado {username.capitalize()}, le deseamos un buen día')
else:
    print('El username no se encuentra en la base de datos')