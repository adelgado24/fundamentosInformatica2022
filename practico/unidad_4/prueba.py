#Anterior intento

accounts = [{'user_id': 'jdelgado', 'password': '25','saving_bank': {'account_num': '2522345', 'amount': float(500)},'current_account':{'account_num':125,'amount':100}, 'last_trxs':[]},
            {'user_id': 'adelgado', 'password': '24','saving_bank': {'account_num': '12341234', 'amount': float(1000)},'current_account':{'account_num':123,'amount':500}, 'last_trxs':[]} ,
            {'user_id': 'mdelgado', 'password': '22','saving_bank': {'account_num': '543253', 'amount': float(500)},'current_account':{'account_num':124,'amount':100}, 'last_trxs':[]},
            {}]
ind = []
print('-----------------\nBanco digital LA\n-----------------')

while True:
    usuario = input('Ingrese su usuario: ')
    contaseña = input('Ingrese su clave: ')
    try:
        for cuenta in accounts:
            if usuario != cuenta['user_id'] or contaseña != cuenta['password']:
                continue
            else:
                logueado = True
                while logueado:
                    indice_de_cuenta = accounts.index(cuenta)
                    ind.append(indice_de_cuenta)
                    opciones = int(input('\nSelecione una operacion:\n1)Acreditar en CA\n2)Acreditar en CC\n3)Consultar saldo en CA\n4)Consultar saldo en CC\n4)Consultar Trx\n6)Salir\n'))
                    if opciones == 1:
                        try:
                            montoCA = float(input('Monto a acreditar: '))
                            accounts[indice_de_cuenta]['saving_bank']['amount'] = montoCA + float(accounts[indice_de_cuenta]['saving_bank']['amount'])
                        except:
                            print('Debe ingresar numeros, vuelva a intentarlo')
                    elif opciones == 2:
                        try:
                            montoCC = float(input('Monto a acreditar: '))
                            accounts[indice_de_cuenta]['current_account']['amount'] = montoCC + float(accounts[indice_de_cuenta]['saving_bank']['amount'])
                        except:
                            print('Debe ingresar numeros, vuelva a intentarlo')
                    elif opciones == 3:
                        print('--Resumen de cuenta--\nNumero de cuenta: ' + str(accounts[indice_de_cuenta]['saving_bank']['account_num'] + '\nMonto: ' + str(accounts[indice_de_cuenta]['saving_bank']['amount'])))
                    elif opciones == 4:
                        print('--Resumen de cuenta--\n' + str(accounts[indice_de_cuenta]['saving_bank']['account_num'] + '\nMonto: ' + str(accounts[indice_de_cuenta]['current_account']['amount'])))
                    elif opciones == 5:
                        print(str(accounts[indice_de_cuenta]['last_trxs']))
                    elif opciones == 6:
                        break
    except:
        print('No se encontro el usuario, verifique los datos')
        pass