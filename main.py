from Paquete.Cliente import Cliente
from Paquete.Usuarios import *

#Ejemplo de uso

cliente1 = Cliente("Julián","Ferrari",23,42283115) # Se crea un cliente

print(f"Fecha de alta de cliente: {cliente1.alta}") # Fecha de alta del cliente

# El cliente realiza compras
cliente1.comprar('Pizza',1500,"Guerrín")
cliente1.comprar('Iphone X 256Gb',250000,"Apple Store")
cliente1.comprar('Curso de programación',25000,"CoderHouse") 

# Verificamos como se encuentran las listas del cliente
print(f"Compras: {cliente1.compras}")
print(f"Devoluciones: {cliente1.devoluciones}\n")

unaCompra = cliente1.compras[1].id # Obtenemos el ID de una compra
cliente1.devolverCompra(unaCompra) # Devolvemos una compra con el mismo ID

# Verificamos como se encuentran las listas despues de la devolución
print(f"\nCompras ahora: {cliente1.compras}")
print(f"Devoluciones ahora: {cliente1.devoluciones}\n")

print(f"Cantidad de compras realizadas: {len(cliente1)}") # Verificamos la cantidad de compras realizadas sin devoluciones