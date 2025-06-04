import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import helpers as help


#Menu principal

print("Menu")
print("1. Crear archivo")
print("2. Listar archivos")
print("3. Abrir archivo")
print("4. Editar archivo")
print("5. Eliminar archivo")
print("6. Salir")

while True:
    case = input("Seleccione una opcion: ")
    if case == '1':
        print("Se ha seleccionado la opcion 1: Crear archivo")
        file_name = input("Ingrese el nombre del archivo a crear: ")
        help.create_file(file_name)

    elif case == '2':
        print("Se ha seleccionado la opcion 2: Listar archivos")
        files = help.list_files()
        print("Archivos en el directorio actual:")
        for file in files:
            print(file)
        
        

    elif case == '3':
        print("Se ha seleccionado la opcion 3: Abrir archivo")
        selec_file = input("Ingrese el nombre del archivo: ")
        help.open_file(selec_file)

    elif case == '4':
        print("Se ha seleccionado la opcion 4: Editar archivo")

    elif case == '5':
        print("Se ha seleccionado la opcion 5: Eliminar archivo")
        nom_file = input("Ingrese el nombre del archivo: ")
        help.delete_file(nom_file)
    
    elif case == '6':
        print("Saliendo del programa...")
        break
        
    else:
        print("Opcion no valida, por favor intente de nuevo.")

