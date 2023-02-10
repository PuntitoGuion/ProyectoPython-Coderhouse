import json
import getpass
import os

# Primera Pre-Entrega

baseDeDatos = {}

def validar(clave):
    """Ingresar una clave para validar que contenga 1 letra mayuscula, 1 letra minuscula, 1 numero y el largo sea de 8 a 16"""

    validacionMayuscula = False
    validacionMinuscula = False
    validacionCantidad = False
    validacionNumerica = False

    for i in range(len(clave)):
        if(clave[i].isupper()):
            validacionMayuscula = True
        if(clave[i].islower()):
            validacionMinuscula = True
        if(clave[i].isnumeric()):
            validacionNumerica = True
    
    if 8<=len(clave)<=16:
        validacionCantidad = True

    resultado = validacionMayuscula and validacionMinuscula and validacionCantidad and validacionNumerica

    if not resultado:
        os.system("cls")
    print("Error!!! Favor de asegurarse que la contraseña contiene al menos un caracter mayúscula, minúscula, númerico y un largo entre 8 y 16")
    return resultado

def pedirUsuario():
    """Pedir usuario al usuario"""

    return input(f"Ingrese usuario: ")

def pedirClave():
    """Pedir clave al usuario"""

    return getpass.getpass("Ingrese contraseña: ")

def exportarDatos(baseDeDatos):
    """Ingresar un diccionario como parametro para exportar la base de datos a un archivo de texto"""
    os.system("cls")
    fileName = input("Ingrese el nombre del archivo: ")
    with open(f"{fileName}.txt",'w') as file_:
        json.dump(baseDeDatos,file_,indent=3)

def importarDatos(baseDeDatos):
    """Ingresar un diccionario como parametro para importar la base de datos desde un archivo de texto"""
    os.system("cls")
    fileName = input("Ingrese el nombre del archivo a importar: ")
    try:
        with open(f"/{fileName}.txt",'r') as file_:
            baseDeDatos.clear()
        for clave,usuario in json.load(file_).items():
            baseDeDatos[clave] = usuario
    except FileNotFoundError:
        print("El archivo no existe")

def registro(baseDeDatos):
    """Ingresar un diccionario como parametro para registrarlo en la base de datos"""

    usuario = pedirUsuario()
    if usuario not in baseDeDatos.keys():
        clave = pedirClave()
        if(validar(clave)):
            os.system("cls")
            baseDeDatos[usuario] = clave
            print(f"El usuario '{usuario}' se ha registrado en la base de datos")
    else:
        print("El usuario ya se ha registrado.")

def mostrarDatos(baseDeDatos):
    """Ingresar un diccionario como parametro para mostrar la base de datos por pantalla"""

    espacios = "                             "
    print("Usuario" + espacios[7 - len(espacios):] + "Clave\n------------------------------------------")
    
    for usuario, clave in baseDeDatos.items():
        separador = espacios[len(usuario)-len(espacios):]
        print(usuario + separador + clave)

def loguear(baseDeDatos):
    """Ingresar un diccionario como parametro para verificar y loguear usuario"""
    
    usuario = pedirUsuario()
    if usuario in baseDeDatos.keys():
        clave = pedirClave()
        if baseDeDatos[usuario]==clave:
            os.system("cls")
            print("Usted pudo loguear correctamente.")
        else:
            print("La clave es incorrecta.")
    else:
        print("El usuario no existe en la base de datos.")


"""Dejo en comentario del menú"""

# while opcion != 6:
#     print("""
#     1 - Registrar usuario en la base de datos
#     2 - Loguear usuario
#     3 - Mostrar base de datos
#     4 - Exportar base de datos
#     5 - Importar base de datos
#     6 - Salir
#     """)
#     try:
#         opcion = int(input())
#         os.system("cls")
#     except ValueError:
#         os.system("cls")
#         print("Error !!! Favor de ingresar un numero")
#         continue
#     if opcion == 1:
#         registro(baseDeDatos)
#     elif opcion == 2:
#         loguear(baseDeDatos)
#     elif opcion == 3:
#         mostrarDatos(baseDeDatos)
#     elif opcion == 4:
#         exportarDatos(baseDeDatos)
#     elif opcion == 5:
#         importarDatos(baseDeDatos)
#     elif opcion == 6:
#         print("El programa finalizó correctamente.")
#     else:
#         print("\nFavor de ingresar una opcion correcta")