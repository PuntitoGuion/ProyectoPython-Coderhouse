from datetime import datetime

# Segunda Pre-Entrega

def obtenerCompra(id:int,compras:list): # Obtengo el objeto Compra en base al ID
    for unaCompra in compras:
        if unaCompra.id == id:
            return unaCompra


class Compra: # Se crea al realizar una compra guardando la fecha, el importe y el nombre del producto.

    validez = True # Validez de una compra

    def __init__(self,producto:str,importe:int,lugar:str,fecha = datetime.today()):
        self.importe = importe
        self.producto = producto
        self.lugar = lugar
        self.id = id(self)
        self.fecha = fecha.strftime("%d/%m/%y") # Fecha de compra con formato DD/MM/YY
        print(f"------------------------------\nDetalles de la compra\nProducto: {self.producto}\nValor: {self.importe}\nSitio: {self.lugar}\nNro de compra: {self.id}\n------------------------------\n")

    def __str__(self): # Sirve para mostrar información del objeto en print
        return f"{self.producto} - ${self.importe}"
    
    def __repr__(self): # Idem que __str__ pero en una lista
        return self.__str__()

    def devolucion(self):
        
        """Se realiza la anulacion de la compra"""

        self.validez = False
        print(f"La compra de {self.producto} ha sido anulada")
        return


class Cliente:

    compras = [] # Compras validas
    devoluciones = [] # Devoluciones

    def __init__(self,nombre:str,apellido:str,edad:int,dni:int,alta=datetime.today()):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni
        self.alta = alta.strftime("%d/%m/%y") # Fecha de alta del cliente en formato DD/MM/YY
    
    def __str__(self): # Muestra información del cliente
        return f"Nombre y apellido: {self.nombre} {self.apellido}\nEdad: {self.edad}\nDNI: {self.dni}"

    def __len__(self): # Cantidad de compras realizadas
        return len(self.compras)

    def comprar(self,producto:str,importe:int,lugar:str):

        """Realiza una compra, indicando el producto y el valor del mismo, agregandola a la lista de compras del cliente"""

        nuevaCompra = Compra(producto,importe,lugar)
        self.compras.append(nuevaCompra)
        return
    
    def devolverCompra(self,id:int):

        """Realizar la devolución de una compra mediante el numero de ID"""

        compra = obtenerCompra(id,self.compras)
        if compra != None:
            compra.devolucion()
            self.compras.remove(compra)
            self.devoluciones.append(compra)
        else:
            print("El ID no existe en las compras realizadas")
        return
