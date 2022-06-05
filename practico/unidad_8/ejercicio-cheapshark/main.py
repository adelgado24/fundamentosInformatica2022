import requests
from Juegos import Juego

tiendas = {}
lista_juegos = []
nombre = input("Ingrese el juego a buscar: ")

def busqueda_juego():
    url2 = "https://www.cheapshark.com/api/1.0/stores"
    response2 = requests.get(url2).json()
    for store in response2:
        tiendas[store["storeID"]] = store["storeName"]

    url = "https://www.cheapshark.com/api/1.0/deals?title="+nombre+"&exact=0&sortBy=Savings&onSale=1"
    response = requests.get(url).json()
    for i in response:
        lista_juegos.append(Juego(i["title"],i["salePrice"],i["normalPrice"],round(float(i["savings"])),tiendas[i["storeID"]]))

def resumen():
    cantidad_juegos = f"Hay {len(lista_juegos)} juegos de {nombre}"
    print("="*len(cantidad_juegos))
    print(cantidad_juegos)
    print("="*len(cantidad_juegos))
    for jueguito in lista_juegos:
        print(jueguito)

busqueda_juego()
resumen()






