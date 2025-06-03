with open('datos.txt', 'w') as f:
    f.write("10,20,30\n")
    f.write("40,50,60\n")
    f.write("70,80,90\n")

with open('datos.txt','r') as archivo:
    datos = archivo.read()
    print(datos)

import os
print(os.getcwd())

total = 0
with open('datos.txt', 'r') as f:
    for linea in f:
        numeros = linea.strip().split(',')  # separa por coma
        for num in numeros:
            total += int(num)

print("Suma total:", total)
