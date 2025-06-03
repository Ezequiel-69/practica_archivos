with open('ejercicio_01.txt', 'w') as archivo:
    archivo.write("Hola, este es un ejemplo de escritura en un archivo.\n")
    archivo.write("Puedes agregar más líneas si lo deseas.\n")


import os

while True:
    print("1. Leer archivo existente")
    print("2. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
            
        archivoIngresar = input("Ingrese el nombre del archivo: ")

        if os.path.exists(archivoIngresar):
            
            print(f"El archivo {archivoIngresar} existe.\n")

            with open(archivoIngresar, 'r') as archivo:
                leer = archivo.read()
                print(leer)
        else:
            print(f"El archivo {archivoIngresar} no existe.")

    elif opcion == '2':
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Intente nuevamente.")
        continue




# with open('ejercicio_01.txt', 'r') as archivo:
#     leer = archivo.read().splitlines()
#     print(leer)

# print("")

# with open('ejercicio_01.txt', 'r') as f:
#     for linea in f:
#         print(linea.strip())
