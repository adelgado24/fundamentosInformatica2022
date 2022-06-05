while True:
    edad = input('Buy a ticket, please enter your age: ')
    try:
        if edad == 'quit':
            break
        elif int(edad) < 5:
            print('Your tickets is free!')
            continue
        elif 5 <= int(edad) < 9:
            print('Your tickets costs 15 USD')
            continue
        elif 9 <= int(edad) <14:
            print('Your ticket costs 23 USD')
            continue
        elif 14<= int(edad) <100:
            print('Your ticket costs 35 USD')
            continue
        elif 100 <= int(edad):
            print("You're awesome!! Free ticket for you")
            continue
    except:
        print("You can't enter letters. Just numbers greater 0")
        continue