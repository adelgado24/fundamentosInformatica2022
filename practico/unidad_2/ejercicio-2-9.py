gustos = [True, False, True, True, True, False, True, False, True, True,
True, False, False, True, True, True, True, False, True, True,
True, False, True, True, False, True, True, False, True, False,
True, True, True, False, True, True, True, False, True, False,
True, True, True, False, False, True, True, True, True, False,
True, True, True, False, True, True, False, True, True, False,
True, False, True, True
]

si_gusto = gustos.count(True)
no_gusto = gustos.count(False)
gusto = si_gusto + no_gusto
gustos_totales = gusto

if (si_gusto/gustos_totales)*100 > 65:
    print(f'PRODUCTO EXITOSO \nAl {(si_gusto/gustos_totales)*100}% les gustó el producto mientras que al {(no_gusto/gustos_totales)*100}% no')
else:
    print(f'PRODUCTO FALLIDO \nAl {(si_gusto/gustos_totales)*100}% les gustó el producto mientras que al {(no_gusto/gustos_totales)*100}% no')