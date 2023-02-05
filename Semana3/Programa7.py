"""   
      Programa7
      Nombre: Marcos Eduardo I. H.
      Fecha: 02/02/2023 
      Descripcion: Realizae en un programa en Python que compare 2 numeros enteros e imprima el mayor de ellos, y si son iguales se umprimira None
"""

numero1 = int(input("Numero 1:"))
numero2 = int(input("Numero 2:"))

if numero1 > numero2:
    print(numero1)
if numero1 < numero2:
    print(numero2)
if numero1 == numero2:
    print(None)