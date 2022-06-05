productos = ["té", "café", "arroz", "harina 000", "lata de tomate", "jabón", "queso pategras", "leche", "levadura",
"desodorante", "detergente", "agua con gas", "trapo de piso", "lavandina", "aceite de oliva", "vinagre",
"mayonesa", "ketchup", "galletas de arroz"
]

buscador = input('¿Qué producto busca?:')

if buscador in productos:
    print(f'Producto en existencia: {buscador}')
else:
    print(f'El proveedor no cuenta con el producto: {buscador}')