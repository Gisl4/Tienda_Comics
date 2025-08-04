# main.py

from models.cliente import Cliente 
from services.tienda import Gestion_tienda
# from colorama import Fore, init
from models.gestion import Comic, realizar_venta, mostrar_catalogo, guardar_catalogo, guardar_ventas
import os

#GLOBAL VARS --------------------------------------------------------------------------------------
# incializamos la tienda de comics como un objeto de la clase tienda a través de su constructor.

def borrar_pantalla():
    # Windows: cls  // Linux/MacOS: clear --> borrar la pantalla
    os.system('cls' if os.name == 'nt' else 'clear')  # ejecuta cls en Windows, clear en otros

def menu_principal():
    print("=============================================")
    print("====  MENÚ PRINCIPAL // TIENDA DE COMICS ====")
    print("=============================================")
    print("1. Gestión de Clientes")
    print("2. Gestión de Tienda (Cómics y Ventas)")
    print("3. Salir")
    print("")

def menu_clientes():
    print("")
    print("INTERFAZ CLIENTES - Define que quieres hacer: ")
    print("1.- Agregar cliente ")
    print("2.- Borrar cliente")
    print("3.- Buscar cliente")
    print("4.- Modificar cliente")
    print("5.- Ver todos los clientes")
    print("")

def menu_tienda():
    print("")
    print("INTERFAZ TIENDA - Define que quiere hacer: ")
    print("1.- Agregar cómic al catálogo")
    print("2.- Ver catálogo de cómics")
    print("3.- Vender cómic a cliente")
    print("4.- Ver historial de compras de un cliente")
    print("5.- Agregar cómic a favoritos de un cliente")
    print("6.- Ver favoritos de un cliente")
    print("")

def fijar_opcion():
    return int(input("Elige la opcion que necesitas: "))

print("")

# Inicialización de la tienda
TiendaComics = Gestion_tienda()

# MENU --------------------------------------------------------------------------------------------
continuar = 's'
while continuar == 's':
    borrar_pantalla()
    menu_principal()
    opcion_principal = fijar_opcion()
    try:
        match opcion_principal:
            case 1:
                menu_clientes()
                opcion = fijar_opcion()
                try:
                    match opcion:
                        case 1:
                            nuevo_cliente = Cliente()
                            nuevo_cliente.agregar_contacto()
                            TiendaComics.agregar_cliente(nuevo_cliente)
                        case 2:
                            TiendaComics.borrar_cliente()
                        case 3:
                            TiendaComics.buscar_cliente()
                        case 4:
                            TiendaComics.modificar_cliente()
                        case 5:
                            TiendaComics.mostrar_clientes()
                        case _:
                            print("Opción no válida.")
                except ValueError:
                    print("Introduce un valor válido.")
                input("Presiona Enter para continuar...")

            case 2:
                menu_tienda()
                opcion = fijar_opcion()
                try:
                    match opcion:
                        case 1:
                            titulo = input("Título del cómic: ")
                            autor = input("Autor: ")
                            genero = input("Género: ")
                            precio = float(input("Precio (€): "))
                            stock = int(input("Cantidad en stock: "))
                            nuevo_comic = Comic(titulo, autor, genero, precio, stock)
                            TiendaComics.catalogo.append(nuevo_comic)
                            print("Cómic agregado al catálogo.")
                            guardar_catalogo(TiendaComics.catalogo)
                        case 2:
                            mostrar_catalogo(TiendaComics.catalogo)
                        case 3:
                            nombre_cliente = input("Nombre del cliente: ")
                            cliente = next((c for c in TiendaComics.clientes if c.nombre.lower() == nombre_cliente.lower()), None)
                            if not cliente:
                                print("Cliente no encontrado.")
                            else:
                                mostrar_catalogo(TiendaComics.catalogo)
                                indice = int(input("Número del cómic a vender: ")) - 1
                                if 0 <= indice < len(TiendaComics.catalogo):
                                    comic = TiendaComics.catalogo[indice]
                                    cantidad = int(input(f"¿Cuántas unidades de '{comic.titulo}' deseas vender?: "))
                                    venta = realizar_venta(cliente, comic, cantidad)
                                    if venta:
                                        TiendaComics.ventas.append(venta)
                                        guardar_ventas(TiendaComics.ventas)
                                        guardar_catalogo(TiendaComics.catalogo)
                                else:
                                    print("Índice fuera de rango.")
                        case 4:
                            nombre = input("Nombre del cliente: ")
                            cliente = next((c for c in TiendaComics.clientes if c.nombre.lower() == nombre.lower()), None)
                            if cliente and cliente.historial:
                                print("\nHistorial de compras:")
                                for venta in cliente.historial:
                                    print(venta)
                            else:
                                print("Sin historial o cliente no encontrado.")
                        case 5:
                            nombre_cliente = input("Nombre del cliente: ")
                            cliente = next((c for c in TiendaComics.clientes if c.nombre.lower() == nombre_cliente.lower()), None)
                            if not cliente:
                                print("Cliente no encontrado.")
                            else:
                                mostrar_catalogo(TiendaComics.catalogo)
                                indice = int(input("Número del cómic a agregar a favoritos: ")) - 1
                                if 0 <= indice < len(TiendaComics.catalogo):
                                    comic = TiendaComics.catalogo[indice]
                                    cliente.agregar_favorito(comic)
                                else:
                                    print("Índice fuera de rango.")
                        case 6:
                            nombre_cliente = input("Nombre del cliente: ")
                            cliente = next((c for c in TiendaComics.clientes if c.nombre.lower() == nombre_cliente.lower()), None)
                            if not cliente:
                                print("Cliente no encontrado.")
                            else:
                                cliente.mostrar_favoritos()
                        case _:
                            print("Opción no válida.")
                except ValueError:
                    print("Introduce un valor válido.")
                input("Presiona Enter para continuar...")

            case 3:
                print("Cerrando programa...")
                break
            case _:
                print("Opción inválida.")
    except ValueError:
        print("Introduce un valor válido.")

    continuar = input("\n¿Quieres continuar? (S/N): ").lower()
