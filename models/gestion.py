# gestion.py

'''
Gestión de los comics y las ventas para la tienda.
'''
from datetime import date

class Comic:
    def __init__(self, titulo, autor, genero, precio, stock):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"Título: {self.titulo} | Autor: {self.autor} | Género: {self.genero} | Precio: {self.precio} € | Stock: {self.stock}"


class Venta:
    def __init__(self, cliente_nombre, comic_titulo, cantidad, total):
        self.cliente_nombre = cliente_nombre
        self.comic_titulo = comic_titulo
        self.cantidad = cantidad
        self.total = total
        self.fecha = date.today()

    def __str__(self):
        return f"{self.fecha} - Cliente: {self.cliente_nombre} - Comic: {self.comic_titulo} x{self.cantidad} - Total: {self.total} €"


# FUNCIONES --------------------------------------------------------------------------------------------------------

def realizar_venta(cliente, comic, cantidad):
    if comic.stock < cantidad:
        print(f"NO se cuenta con stock suficiente para '{comic.titulo}'... Quedan {comic.stock} unidades.")
        return None
    total = comic.precio * cantidad
    comic.stock -= cantidad

    venta = Venta(cliente.nombre, comic.titulo, cantidad, total)

    # Si se tiene cliente se "GUARDA"
    if hasattr(cliente, "historial"):
        cliente.historial.append(venta)
    else:
        cliente.historial = [venta]

    print(f"Venta realizada {cantidad} unidad(es) de '{comic.titulo}' para {cliente.nombre}. Total: {total} €")
    return venta


def mostrar_catalogo(catalogo):
    if not catalogo:
        print("NO existen cómics en el catálogo.")
    else:
        print("\nCatálogo de Cómics:")
        for idx, comic in enumerate(catalogo, start=1):
            print(f"{idx}. {comic}")


# === PERSISTENCIA EN ARCHIVOS ===
import os
from datetime import date as _date

DATA_DIR = "data"
CATALOGO_FILE = os.path.join(DATA_DIR, "catalogo.txt")
VENTAS_FILE   = os.path.join(DATA_DIR, "ventas.txt")


def cargar_catalogo():
    comics = []
    if not os.path.exists(CATALOGO_FILE):
        return comics
    with open(CATALOGO_FILE, "r", encoding="utf-8") as f:
        for linea in f:
            titulo, autor, genero, precio, stock = linea.strip().split(";")
            comics.append(Comic(titulo, autor, genero, float(precio), int(stock)))
    return comics


def guardar_catalogo(catalogo):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(CATALOGO_FILE, "w", encoding="utf-8") as f:
        for c in catalogo:
            f.write(f"{c.titulo};{c.autor};{c.genero};{c.precio};{c.stock}\n")


def cargar_ventas():
    ventas = []
    if not os.path.exists(VENTAS_FILE):
        return ventas
    with open(VENTAS_FILE, "r", encoding="utf-8") as f:
        for linea in f:
            fecha_str, cliente_nombre, comic_titulo, cantidad, total = linea.strip().split(";")
            v = Venta(cliente_nombre, comic_titulo, int(cantidad), float(total))
            v.fecha = _date.fromisoformat(fecha_str)
            ventas.append(v)
    return ventas


def guardar_ventas(ventas):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(VENTAS_FILE, "w", encoding="utf-8") as f:
        for v in ventas:
            f.write(f"{v.fecha.isoformat()};{v.cliente_nombre};{v.comic_titulo};{v.cantidad};{v.total}\n")
