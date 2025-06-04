#Funciones

import os

#Crear archivos
def create_file(file_path):
    with open(file_path, 'w') as file:
        pass
    print(f'Archivo {file_path} creado correctamente.')

#Listar archivos
def list_files(directory='.'):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

#Abrir archivos
def open_file(file_path):
    with open(file_path, 'r') as file:
        contenido = file.read()
        print(contenido)

#Editar archivos

#Eliminar archivos
def delete_file(file_path):
    file_path = os.remove(file_path)
    print(f"Archivo {file_path} eliminado correctamente.")
    print(file_path)

