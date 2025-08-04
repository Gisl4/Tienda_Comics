# tienda.py
'''
Estructura de la tienda con referencias a las clases que definen los distintos parámetros a guardar:

    1.- clientes
    2.- proveedores....
'''

import os
from models.cliente import Cliente, cargar_clientes, guardar_clientes

# Carpeta donde se guardan los datos
DATA_DIR = "data"

class Gestion_tienda:
    # Contructor: definición de los atributos del objeto ---------------------------------------------------------
    def __init__(self):
        # Asegura que exista la carpeta de datos
        os.makedirs(DATA_DIR, exist_ok=True)
        # Carga clientes desde disco
        self.clientes = cargar_clientes()
        # Inicializa catálogo y ventas (opcionalmente cargar de persistencia si lo deseas)
        self.catalogo = []
        self.ventas   = []

    # METODOS --------------------------------------------------------------------------------------------------------

    def agregar_cliente(self, cliente):
        # a la lista de clientes definida en el init, le añado el "objeto" cliente
        self.clientes.append(cliente)
        # Persistir cambios
        guardar_clientes(self.clientes)
        print(f"✔ Cliente {cliente.nombre} añadido y guardado.")

    def borrar_cliente(self):
        nombre_buscar = input ("Introduce el nombre de cliente a buscar: ")
        encontrado = False
        for i, cliente in enumerate(self.clientes):
            if cliente.nombre.lower() == nombre_buscar.lower():
                del self.clientes[i]
                print(f"¡El cliente {nombre_buscar} ha sido borrado!")
                # Persistir cambios
                guardar_clientes(self.clientes)
                encontrado = True
                break
        if not encontrado:
            print ("--- ### El cliente solicitado no existe en la agenda ## --- ")  

    def buscar_cliente(self):
        nombre_buscar = input ("Introduce el nombre a buscar: ")
        encontrado = False
        for cliente in self.clientes:
            if cliente.nombre.lower() == nombre_buscar.lower():
                # traducimos el código de membresía a texto
                tipo = Cliente.MEMBRESIAS_TIPO.get(cliente.membresia, "Desconocida")
                print(
                    f"Encontrado:\n"
                    f" ·Nombre: {cliente.nombre}\n"
                    f" ·Edad: {cliente.edad}\n"
                    f" ·Email: {cliente.email}\n"
                    f" ·Teléfono: {cliente.tlf}\n"
                    f" ·Dirección: {cliente.dir}\n"
                    f" ·Membresía: {tipo}\n"
                    f" ·Fecha registro: {cliente.fecha_registro}"
                )
                encontrado = True
                break
        if not encontrado:
            print ("--- ### Cliente no existe en la tienda ## --- ")

    def modificar_cliente(self):
        nombre_buscar = input ("Introduce el nombre a buscar: ")
        encontrado = False
        for cliente in self.clientes:
            if cliente.nombre.lower() == nombre_buscar.lower():
                encontrado = True
                # Mostramos estado actual
                tipo_actual = Cliente.MEMBRESIAS_TIPO.get(cliente.membresia, "Desconocida")
                print(f"Encontrado: ·Nombre: {cliente.nombre}\n ·Edad: {cliente.edad}\n ·Email: {cliente.email}\n ·Teléfono: {cliente.tlf}\n ·Dirección: {cliente.dir}\n ·Membresía: {tipo_actual}\n ·Fecha registro: {cliente.fecha_registro}")
                # edad --> ¿actualizamos?
                print (f"Edad actual: {cliente.edad} --> ¿Actualizar edad?")
                nueva_edad = input(f"(Introduce el valor nuevo o pulsa Enter para mantener actual) ")
                # email --> ¿Actualizamos?
                print (f"Email actual: {cliente.email} --> ¿Actualizar email?")
                nuevo_email = input(f"(Introduce el valor nuevo o pulsa Enter para mantener actual): ")
                # membresía --> ¿Actualizamos?
                print ("Membresia actual: 1.- Premium 2.- Estándar 3.- Inactivo")
                print (f"[{cliente.membresia}] --> ¿Actualizar membresía?")
                nueva_membresia = input(f"(Introduce el valor nuevo o pulsa Enter para mantener actual) ")
                # teléfono --> ¿Actualizamos?
                while True:
                    print (f"Teléfono actual: {cliente.tlf} --> ¿Actualizar teléfono?")
                    nuevo_telefono = input(f"(Introduce el valor nuevo o pulsa Enter para mantener actual): ")
                    if nuevo_telefono and len(nuevo_telefono) != 9:
                        print ("## Error ## ¡Nº Telefono introducido no válido! (9 dígitos)")
                    else:
                        break
                # dirección --> ¿Actualizamos?
                print (f"Dirección actual: {cliente.dir} --> ¿Actualizar dirección?")
                nueva_direccion = input(f"(Introduce el valor nuevo o pulsa Enter para mantener actual) ")
                # Aplicar cambios
                if nueva_edad:
                    cliente.edad = int(nueva_edad)
                if nuevo_email:
                    cliente.email = nuevo_email
                if nueva_membresia:
                    cliente.membresia = int(nueva_membresia)
                if nuevo_telefono:
                    cliente.tlf = nuevo_telefono
                if nueva_direccion:
                    cliente.dir = nueva_direccion
                # Mostrar resumen
                print(f"¡Contacto Actualizado:")
                print(f"Nombre: {cliente.nombre}")
                print(f"Edad: {cliente.edad}")  
                print(f"Email: {cliente.email}")
                tipo_nuevo = Cliente.MEMBRESIAS_TIPO.get(cliente.membresia, "Desconocida")
                print(f"Membresía: {tipo_nuevo}")
                print(f"Teléfono: {cliente.tlf}")
                print(f"Dirección: {cliente.dir}")
                # Persistir cambios
                guardar_clientes(self.clientes)
                print("✔ Cliente modificado y guardado.")
                break
        if not encontrado:
            print ("--- ### Cliente no existe en la tienda ## --- ")

    def mostrar_clientes(self): #aqui ya tengo cliente metido en la lista
        if not self.clientes:
            print ("Sin datos de clientes.")
        for cliente in self.clientes:
            print (cliente)
