orders = []

while True:
    print("Farmacia - Opciones:")
    print("\t(1) Agregar")
    print("\t(2) Listar")
    print("\t(3) Salir")

    option = input(">> ")
    if option == "3":
        break

    if option == "1":
        item = {}

        print("Nombre del medicamento")
        medicine = input(">> ")

        print("Nombre del laboratorio")
        lab = input(">> ")

        print("Cantidad")
        quantity = input(">> ")

        item['medicamento'] = medicine
        item['laboratorio'] = lab
        item['quantity'] = quantity

        if item in orders:
            print("Medicamento existente")
        else:
            orders.append(item)

    elif option == "2":
        print(f"\nOrdenes: {orders}")

    else:
        print(f"La opcion ({option}) no es valida")
