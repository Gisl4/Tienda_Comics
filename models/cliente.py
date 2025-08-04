# cliente.py
'''
Definición de la clase cliente.
'''

import os
from datetime import date

DATA_DIR = "data"
CLIENTES_FILE = os.path.join(DATA_DIR, "clientes.txt")

# CLASES --------------------------------------------------------------------------------------------------------

class Cliente:
    MEMBRESIAS_TIPO = {
        1: "Premium",
        2: "Estándar",
        3: "Inactivo"
    }

    # Contructor: definición de los atributos del objeto ---------------------------------------------------------
    def __init__(self):
        self.nombre = ''
        self.edad = ''
        self.email = ''
        self.membresia = '' 
        self.tlf = ''
        self.dir = ''
        self.favoritos = []  # agregado
        self.fecha_registro = ''     
        self.historial = []

    # METODOS ---------------------------------------------------------------------------------------------------------
    # metodo para imprimir los atributos del objeto de forma inteligible
    def __str__(self):
        tipo_membresia = self.MEMBRESIAS_TIPO.get(self.membresia, "Desconocida")
        return (f" Nombre: {self.nombre}\n Edad: {self.edad}\n Email: {self.email}\n Teléfono: {self.tlf}\n Dirrección: {self.dir}\n Membresia: {tipo_membresia}\n Fecha registro: {self.fecha_registro}")
          
    
    def agregar_contacto(self):
        self.nombre = input ("Introduce el nombre del cliente: ")
        self.edad = int(input ("Introduce edad del cliente: "))
        # Email con comprobación
        while True:
            self.email = input (f"Introduce el email de {self.nombre}: ")
            arroba = 0
            for caracter in self.email:
                # si encuentra una arroba, suma 1
                if caracter == "@":
                    arroba += 1
            # si no contiene una arroba o contiene mas de una...        
            if arroba != 1:     
                print (f" #### ERROR ### \n No se ha introducido un formato de email valido")
            else:
                print ("## ¡Email introducido valido! ##")
                break
        # Membresía          
        print("Selecciona tipo de membresía:")
        print("1.- Premium")
        print("2.- Estándar")
        print("3.- Inactivo")
        self.membresia = int(input ("Introduce tipo de membresía: ")) 
        # Si el tamaño telefono es distinto de 9 digitos, bucle hasta que lo metas bien
        while True:
            telefono = input (f"Introduce el teléfono de {self.nombre} (9 digitos): ")    
            if len (telefono) == 9:
                self.tlf = telefono
                break
            else:
                print ("## Error ## ¡Nº Telefono no válido! (9 digitos)")
                
        self.dir = input (f"Introduce la dirección de {self.nombre}: ")
        self.fecha_registro = date.today()   
                    
# FAVORITOS --------------------------------------------------------------------------------------------------------- 

    def agregar_favorito(self, comic):
        if comic not in self.favoritos:
            self.favoritos.append(comic)
            print(f"'{comic.titulo}' añadido a favoritos.")
        else:
            print(f"'{comic.titulo}' ya se encuentra en favoritos.")

    def mostrar_favoritos(self):
        if not self.favoritos:
            print("El cliente NO tiene cómics favoritos.")
        else:
            print(f"Favoritos de {self.nombre}:")
            for idx, comic in enumerate(self.favoritos, start=1):
                print(f"{idx}. {comic}")

    def eliminar_favorito(self, comic):
        if comic in self.favoritos:
            self.favoritos.remove(comic)
            print(f"'{comic.titulo}' se ha eliminado de favoritos.")
        else:
            print(f"'{comic.titulo}' no se encuentra en la lista de favoritos.")

# === PERSISTENCIA CLIENTES ===

def cargar_clientes():
    clientes = []
    if not os.path.exists(CLIENTES_FILE):
        return clientes
    with open(CLIENTES_FILE, "r", encoding="utf-8") as f:
        for linea in f:
            nombre, edad, email, memb_str, tlf, direccion, fecha = linea.strip().split(";")
            c = Cliente()
            c.nombre = nombre
            c.edad = int(edad)
            c.email = email
            inv = {v: k for k, v in Cliente.MEMBRESIAS_TIPO.items()}
            c.membresia = inv.get(memb_str, 3)
            c.tlf = tlf
            c.dir = direccion
            c.fecha_registro = fecha
            c.favoritos = []
            c.historial = []
            clientes.append(c)
    return clientes


def guardar_clientes(clientes):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(CLIENTES_FILE, "w", encoding="utf-8") as f:
        for c in clientes:
            memb_str = Cliente.MEMBRESIAS_TIPO.get(c.membresia, "Inactivo")
            f.write(f"{c.nombre};{c.edad};{c.email};{memb_str};{c.tlf};{c.dir};{c.fecha_registro}\n")
