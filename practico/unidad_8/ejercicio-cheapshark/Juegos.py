class Juego:
    def __init__(self,nombre, precio_descuento,precio_original,descuento,tiendas):
        self.nombre = nombre
        self.precio_descuento = precio_descuento
        self.descuento = descuento
        self.precio_original = precio_original
        self.tiendas = tiendas

    def __str__(self):
        return f"-------------------------\nJuego: {self.nombre}\nTiene un descuento de {float(self.descuento)}%" \
               f"\nprecio original: $ {round(float(self.precio_original),2)}\nprecio con descunto: $ {round(float(self.precio_descuento),2)}" \
               f"\nEl juego se encuentra en: {self.tiendas}"



